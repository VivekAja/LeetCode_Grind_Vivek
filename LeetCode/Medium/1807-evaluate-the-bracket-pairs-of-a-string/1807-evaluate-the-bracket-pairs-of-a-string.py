class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knmap = { key: value for key, value in knowledge}

        result = []
        temp  = ""
        inside = False

        for a in s:
            if a == "(":
                inside = True
                temp = ""
            elif a == ")":
                value = knmap.get(temp, "?")
                result.append(value)
                inside = False
            elif inside:
                temp +=a
            else:
                result.append(a)

        return "".join(result)