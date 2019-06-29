### 스킬

# 맞는 각에서 구멍의 폭을 계산. 폭이 가장 넓은 쪽으로 보내기


from math import *

# 가는 길에 다른 공이 있는지 판단하는 함수(치는 공, 타겟 공, 중간의 공)
def judge_ball_in_way(hit, target, other):
    print("hit", hit, "target", target, "other", other)
    judge = False
    hit_x, hit_y = hit[0], hit[1]
    target_x, target_y = target[0], target[1]
    other_x, other_y = other[0], other[1]
    # hit과 target의 중심점을 잇는 직선의 방정식을 구하고, 그것을 평행이동하여 친 공의 진로 범위를 구할 것
    # z는 두 원점을 잇는 직선의 거리, k는 중심점 잇는 직선을 평행이동하는 정도, a는 두 원점을 잇는 직선의 기울기
    z = sqrt((hit_x - target_x) ** 2 + (hit_y - target_y) ** 2)
    k = radius * z / abs(hit_y - target_y)
    a = (hit_y - target_y) / (hit_x - target_x)
    # 공의 위치에 따라 if문 분기하여 진로 내에 다른 공이 있는지 판단
    ## hit과 target의 위치 판단
    print(other_y, a, other_x, hit_x, k, hit_y, other_y, "hello")
    ### 두 공이 좌상-우하의 배치에 있을 때
    if (hit_x < target_x and hit_y > target_y) or (hit_x > target_x and hit_y < target_y):
        # 범위 내에 공이 위치하는지 판단
        if other_y < a * (other_x - hit_x - 2*k) + hit_y and other_y > a * (other_x - hit_x + 2*k):
            judge = True
    ### 두 공이 좌하-우상의 배치에 있을 때
    elif (hit_x > target_x and hit_y > target_y) or (hit_x < target_x and hit_y < target_y):
        if other_y > a * (other_x - hit_x - 2*k) + hit_y and other_y < a * (other_x - hit_x + 2*k) + hit_y:
            print("안됨")
            judge = True
    # 두 공이 수직으로 위치할 때
    elif hit_x == target_x:
        if hit_x - 2*radius < other_x < hit_x + 2*radius and (hit_y < other_y < target_y or target_y < other_y < hit_y):
            judge = True
    # 두 공이 수평으로 위치할 때
    elif hit_y == target_y:
        if hit_y - 2*radius < other_y < hit_y + 2*radius and (hit_x < other_x < target_x or target_x < other_x < hit_x):
            judge = True
    # else: # 이외의 경우가 있는지 잘 모르겠음. 혹시를 대비해 아무렇게나 막 치게 만들어도 좋을 듯
    return judge


def find_power_direction(hit, target, hole):
    target_x, target_y = target[0], target[1]
    hole_x, hole_y = hole
    # target공이 구멍 들어가는 각에 가장 가까운 각 찾기
    min_diff_angle = 10000000
    min_diff = 100000000
    # 360도를 돌면서
    for angle in range(0, 91):
        # 라디안 단위로 변환
        rad = radians(angle)
        # 각도로 돌면서 찾는 탄젠트 값과, 실제 공과 구멍 사이의 직각삼각형 탄젠트 값이 가장 가까운 각도 찾기
        delta_x = hole_x - target_x
        delta_y = hole_y - target_y
        this_diff = abs(tan(rad) - abs(delta_y) / abs(delta_x))
        if this_diff < min_diff:
            min_diff = this_diff
            min_diff_angle = angle
    print(min_diff_angle)
    # hole과 target의 상대적 위치에 따라 절대 각도(360도 기준) 다르게 구하기
    ## 우상단
    if delta_x >= 0 and delta_y >= 0:
        abs_diff_angle = 90 - min_diff_angle
    ## 우하단
    elif delta_x >= 0 and delta_y < 0:
        abs_diff_angle = 90 + min_diff_angle
    ## 좌상단
    elif delta_x < 0 and delta_y >= 0:
        abs_diff_angle = 270 + min_diff_angle
    ## 좌하단
    elif delta_x < 0 and delta_y < 0:
        abs_diff_angle = 270 - min_diff_angle


    # target 공이 min_diff_angle의 각으로 갈 수 있도록 큐(당구대)로 쳐야하는 hit 공 각도 찾기
    ## hit 공이 도달해야 하는 지점 구하기(직각삼각형 닮은꼴 이용))
    hole_distance = sqrt((target_x - hole_x) ** 2 + (target_y - hole_y) ** 2)
    height = radius * abs(target_y - hole_y) / hole_distance
    ## hit 공의 도달 지점을 구멍 위치에 따라 다르게 구하기
    ### 좌하, 좌상일 때의 x 구하기
    if hole_idx == 0 or hole_idx == 3:
        hitting_x = target_x + sqrt((2 * radius) ** 2 - (2 * height) ** 2)
    ### 우하, 우상일 때의 x 구하기
    elif hole_idx == 2 or hole_idx == 5:
        hitting_x = target_x - sqrt((2 * radius) ** 2 - (2 * height) ** 2)
    ### 중하, 중상일 때의 x 구하기
    else:
        if target_x < hole_x:
            hitting_x = target_x - sqrt((2 * radius) ** 2 - (2 * height) ** 2)
        else:
            hitting_x = target_x + sqrt((2 * radius) ** 2 - (2 * height) ** 2)
    if hole_idx == 0 or hole_idx == 1 or hole_idx == 2:
        hitting_y = target_y + 2 * height
    else:
        hitting_y = target_y - 2 * height

    can_hit = True
    for i in range(1, 10):
        other = balls[i]
        print("hole", hole, "other", other)
        if judge_ball_in_way(hit, [hitting_x, hitting_y], other):
            can_hit = False
            print("cannot hit")
            return

    ## hit 공 치는 각도 구하기
    ### hit distance
    delta_x = hit_x - hitting_x
    delta_y = hit_y - hitting_y
    hit_distance = sqrt(delta_x ** 2 + delta_y ** 2)
    
    min_hit_angle = 100000000
    min_hit_diff = 1000000
    ### 360도 돌면서 탄젠트 값이 delta_y/delta_x와 가장 비슷한 각도 찾기
    for angle in range(0, 360):
        rad = radians(angle)
        this_diff = abs(tan(rad) - abs(delta_y/delta_x))
        if this_diff < min_diff:
            min_diff = this_diff
            min_hit_angle = angle
    # hit 공이 우상단에 위치
    if delta_x >= 0 and delta_y >= 0:
        result_angle = 270 - min_hit_angle
    # 우하단
    elif deta_x >= 0 and delta_y < 0:
        result_angle = 270 + min_hit_angle
    # 좌상단
    elif delta_x < 0 and delta_y >= 0:
        result_angle = 90 + min_hit_angle
    # 좌하단
    elif delta_x < 0 and delta_y < 0:
        result_angle = 90 - min_hit_angle

    # target에서 hole까지 가는 데 필요한 힘 찾기(거리 비례)
    # hit에서 target까지 가는 데 필요한 힘 찾기(거리 비례)
    theta_angle = abs(result_angle - abs_diff_angle)
    theta = radians(theta_angle) # 라디안으로 변환
    # alpha = 거리-힘 계수
    alpha = 1
    power = (alpha * (hole_distance + hit_distance)) / (1 + cos(theta))
    return result_angle, power, min_diff_angle  # hit 공을 치는 절대각도(360도 기준), 파워, target공이 구멍으로 들어가는 각도



# 변수 초기화
# radius: 공의 반지름, balls: 10개 공의 정보 리스트, hit_*: 치는 공(접두사), target_*: 맞추려는 공(접두사)
radius = 10
# index: 공의 번호, [x좌표, y좌표, 구멍에 넣었는지 여부], 0번째 공이 흰색 공
balls = [[10, 50], [94, 55, False]]
num_ball = len(balls)
hole_radius = 10
# 포켓 좌표(좌하, 하, 우하, 좌상, 상, 우상)
holes = [[0, 0], [100, 0], [200, 0], [0, 100], [100, 100], [200, 100]]

# 쳐야하는 흰 공
hit = balls[0]
hit_x, hit_y = hit

# 맞춰야 하는 공 고르기 - 번호(index)가 작은 공부터 맞춰야하므로 index가 작은 공부터 탐색해서 구멍에 들어가지 않은 공을 찾는다.
for i in range(1, num_ball):
    if not balls[i][2]:
        idx_target = i
        target = balls[i]
        target_x, target_y = target[0], target[1]
        break
print("target", target)
# else: 공을 다 넣었을 때 처리해주기


# 1. 직접적으로 한 공 맞춰서 넣기
# target 공으로 가는 길에 다른 공이 없을 때
# (x1, y1)과 (x2, y2)를 지나는 방정식에서 폭을 +-radius만큼 더해준 범위 내에 다른 공이 있는지 판단
# 다른 공이 있다면 2.로 분기
ball_in_way = False
for i in range(1, num_ball):
    if i != idx_target and judge_ball_in_way(hit, target, balls[i]):
        ball_in_way = True
        break

if not ball_in_way:
    print("no ball in way")
    # 6개 구멍에 대해 가장 들어갈 확률이 높은 구멍 찾기
    results = []
    for hole_idx in range(6):
        hole = holes[hole_idx]
        # 구멍까지 가는 길에 다른 공 없는지 판단
        ball_in_way_hole = False
        for i in range(1, num_ball):
            if i != idx_target and judge_ball_in_way(target, hole, balls[i]):
                ball_in_way_hole = True
                break
        # 구멍까지 가는 길에 다른 공이 있으면
        if ball_in_way_hole:
            # 다음 구멍 탐색
            continue
        # 가는 길에 다른 공이 없으면 직접적으로 맞추기
        else:
            # 흰공이 빠지지 않게(미구현)
            # 최적 각도, 파워, 구멍 입사각 구하기
            result = find_power_direction(hit, target, hole)
            print("result: ", result)
            if result:
                angle, power, hole_angle = result
                # hole 위치에 따라 각도 보정
                ## 코너에 있는 구멍일 때 45도 기준으로 차이 구하기
                if hole_idx == 0 or hole_idx == 2 or hole_idx == 3 or hole_idx == 5:
                    diff_angle = abs(45 - hole_angle)
                ## 중간에 있는 구멍일 때 90도 기준으로 차이 구하기
                else:
                    diff_angle = abs(90 - hole_angle)
                results.append([angle, power, diff_angle])
    # 가장 들어갈 확률이 높은 구멍(diff_angle이 0에 가까운 구멍 선택)
    print("result", results)
    if results:
        print(sorted(results, key=lambda x: x[2])[0])



# 그게 아니면
# else:
# 2. 쿠션을 통해 한 공 맞춰서 넣기(일단 1쿠션만 고려)
# 4개의 벽에 대해 target 공으로 가는 길에 다른 공이 없는 루트의 벽을 찾기
# 벽에 맞았을 때를 시점에서 1.과 동일한 함수를 통해 필요한 힘을 계산.
# 벽 충돌의 영향까지 고려한 초기 힘값 도출
# 4개의 벽 모두에 대해 쿠션으로 넣는 것이 불가능한 경우 3.으로 분기



# 3. 한 공을 넣을 수 없을 경우, 공을 맞춰서 다른 공 넣기
# 한 공을 맞추고 난 직후 '맞춘 공'의 초기 상태를 기준으로 1.에서와 동일한 함수 사용 -> 가야하는 방향과 필요한 힘을 계산
