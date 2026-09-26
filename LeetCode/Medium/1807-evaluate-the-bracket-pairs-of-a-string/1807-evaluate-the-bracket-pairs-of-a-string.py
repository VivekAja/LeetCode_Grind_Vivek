class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knmap ={key:value for key, value in knowledge}
        inside = False
        temp = ""
        result = []

        for c in s:
            if c == "(":
                inside = True
                temp = ""
            elif c == ")":
                value = knmap.get(temp, "?")
                result.append(value)
                inside = False
            elif inside:
                temp +=c
            else:
                result.append(c)

        return "".join(result)