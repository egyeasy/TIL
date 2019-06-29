# 괄호 () 뿐일 때



# # 괄호 ({[ 있을 때
# def find_bracket(chr):
#     brackets = '(){}[]'
#     for i in range(len(brackets)):
#         if brackets[i] == chr:
#             return brackets[i - 1]
#
#
# def bracket(word):
#     stack = [""]*len(word)
#     top = -1
#     for c in word:
#         if c == '(' or c == '{' or c == '[':
#             stack[top + 1] = c
#             top += 1
#         if c == ')' or c == '}' or c == ']':
#             if top == -1:
#                 return False
#             else:
#                 if stack[top] == find_bracket(c):
#                     pop
#                 else:
#                     return False
#
#     if stack[top + 1] != "":
#         return False
#     else:
#         return True