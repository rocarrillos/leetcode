class Solution:
    def isValid(self, s: str) -> bool:
        lastOpened = []
        for item in s:
            if item in ["(", "{", "["]:
                lastOpened.append(item)
            else:
                if len(lastOpened) == 0:
                    return False
                if item == ")":
                    if lastOpened[-1] == "(":
                        lastOpened.pop(-1)
                    else:
                        return False
                if item == "}":
                    if lastOpened[-1] == "{":
                        lastOpened.pop(-1)
                    else:
                        return False
                if item == "]":
                    if lastOpened[-1] == "[":
                        lastOpened.pop(-1)
                    else:
                        return False
        if len(lastOpened) == 0:
            return True
