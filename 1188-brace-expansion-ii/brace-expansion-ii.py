class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        i = 0
        n = len(expression)

        def product(a, b):
            return {x + y for x in a for y in b}

        def parse_expression():
            nonlocal i

            # expression = term (, term)*
            result = parse_term()

            while i < n and expression[i] == ',':
                i += 1
                result |= parse_term()

            return result

        def parse_term():
            nonlocal i

            # empty string is identity for concatenation
            result = {""}

            while i < n and expression[i] not in '},':
                factor = parse_factor()
                result = product(result, factor)

            return result

        def parse_factor():
            nonlocal i

            if expression[i].isalpha():
                ch = expression[i]
                i += 1
                return {ch}

            # expression[i] == '{'
            i += 1                      # skip {
            result = parse_expression()
            i += 1                      # skip }

            return result

        ans = parse_expression()

        return sorted(ans)