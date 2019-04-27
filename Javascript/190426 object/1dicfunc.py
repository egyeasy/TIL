def poop():
    return "poop"
    
donghoon = {
    'name': 'donghoon',
    # 'poop': lambda : 'poop'  // 이렇게도 쓸 수 있고
    'poop': poop
    
}

print(donghoon['poop'])
print(donghoon['poop']())