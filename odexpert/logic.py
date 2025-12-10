import sympy as sp
import math
import re

class FinalHomoExact:
    def extract_variables(self, dx, dy):
        equation = dx + " " + dy  
        return sorted(set(re.findall(r'\b[x-y]\w*\b', equation)))

    def parse_and_scale(self, dx, dy, vars, scale_factor=1):
        scaled_equation_dx = dx
        scaled_equation_dy = dy
        for var in vars:
            scaled_equation_dx = scaled_equation_dx.replace(var, f"({scale_factor}*{var})")
            scaled_equation_dy = scaled_equation_dy.replace(var, f"({scale_factor}*{var})")
        return scaled_equation_dx, scaled_equation_dy

    def normalize_roots(self, equation):
        equation = re.sub(r'\bsqrt\((.*?)\)', r'sp.sqrt(\1)', equation)
        equation = re.sub(r'\bcbrt\((.*?)\)', r'(\1)**(1/3)', equation)  
        equation = re.sub(r'\b(\d+)\.rt\((.*?)\)', r'(\2)**(1/\1)', equation) 
        return equation

    def root_de(self, dx, dy):
        dx = self.normalize_roots(dx)
        dy = self.normalize_roots(dy)
        return dx, dy

    def is_homogeneous(self, dx, dy):
        dx, dy = self.root_de(dx, dy)

        dx = dx.replace("^", "**").replace("e", "math.e").replace("ln", "sp.log")
        dy = dy.replace("^", "**").replace("e", "math.e").replace("ln", "sp.log")

        vars = self.extract_variables(dx, dy)
        if not vars:
            return False, None

        degree = None

        original_eval_dx = eval(dx, {"sp": sp, "math": math}, {var: 1 for var in vars})
        original_eval_dy = eval(dy, {"sp": sp, "math": math}, {var: 1 for var in vars})
       
        for t in [2, 3, 4]:
            scaled_dx, scaled_dy = self.parse_and_scale(dx, dy, vars, scale_factor=t)

            try:
                scaled_eval_dx = eval(scaled_dx, {"sp": sp, "math": math}, {var: 1 for var in vars})
                scaled_eval_dy = eval(scaled_dy, {"sp": sp, "math": math}, {var: 1 for var in vars})
            except Exception as e:
                return False, None

            if scaled_eval_dx == 0 and scaled_eval_dy == 0:
                continue

            if scaled_eval_dx != 0 and scaled_eval_dy != 0:
                computed_degree_dx = round(math.log(abs(scaled_eval_dx/original_eval_dx), t))
                computed_degree_dy = round(math.log(abs(scaled_eval_dy/original_eval_dy), t))

                if degree is None:
                    degree = computed_degree_dx if computed_degree_dx == computed_degree_dy else None
                elif degree != computed_degree_dx or degree != computed_degree_dy:
                    return False, None

        if degree is None:
            return False, None

        return True, degree

    def isHomo(self, dx, dy):
        x, y, lam = sp.symbols('x y lam')

        if any(substring in dx or substring in dy for substring in ['sqrt', 'cbrt', '.rt', 'log', 'ln', "(5/3)", "(5/2)", "(3/2)"]):
            result, degree = self.is_homogeneous(dx, dy)
            if result:
                return True, degree
            else:
                return False
        else:
            lambda_m = dx.replace("x", "(lam*x)")
            lambda_m = lambda_m.replace("y", "(lam*y)")

            lambda_n = dy.replace("x", "(lam*x)")
            lambda_n = lambda_n.replace("y", "(lam*y)")

            lambda_m = sp.sympify(lambda_m)
            lambda_m = sp.simplify(lambda_m)

            mcpy = lambda_m

            lambda_n = sp.sympify(lambda_n)
            lambda_n = sp.simplify(lambda_n)

            m = sp.sympify(dx)
            n = sp.sympify(dy)

            m_n = m / n
            m_n = sp.simplify(m_n)

            lam_m_lam_n = lambda_m / lambda_n
            lam_m_lam_n = sp.simplify(lam_m_lam_n)

            if m_n == lam_m_lam_n:
                mcpy = mcpy / m

                degree = sp.total_degree(mcpy)

                return True, degree
            else:
                return False, None

    def is_exact(self, M, N):

        x, y, c = sp.symbols('x y C')

        dy = sp.diff(M, y)

        dx = sp.diff(N, x)

        ans = sp.simplify(dy - dx)

        if ans == 0:
            return True
        else:
            return False

    def solve_exact(self, m, n):
        x, y, c = sp.symbols('x y C')

        dy = sp.diff(m, y)


        dx = sp.diff(n, x)

        integ_x = sp.integrate(m, x)
        integ_y = sp.integrate(n, y) - integ_x.diff(y)
        ans = integ_x + integ_y

        final_ans = sp.Eq(ans, c)

        return integ_x, integ_y, final_ans, dy, dx
