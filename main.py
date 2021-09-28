from env import *
from tqdm import tqdm

#
#
# # def check_end_game():
# #     for key, item in game_dict.items():
# #         if item['direction'] != 1:
# #             return True
# #
# #     return False
#
#
# env = CustomEnv()
# env.init_render()
# done = False
#
# for episode in range(100):
#     env.clock.tick(30)
#
#     env.render()
#
#     #
#     # for event in pygame.event.get():
#     #     if event.type == pygame.QUIT:
#     #         done = True
#         # if event.type == pygame.MOUSEBUTTONDOWN:
#         #     if pygame.mouse.get_pressed(3) == (1, 0, 0):
#                 # timer_started = True
#                 # if timer_started:
#                 #     start_time = pygame.time.get_ticks()
#     action = env.action_space.sample()
#     obs, reward, done, _ = env.step(action)
#
# # print("Score final : ", str(passed_time / 1000))
#
# pygame.quit()

# 1. Load Environment and Q-table structure
env = CustomEnv()
env.init_render()
Q = np.zeros([env.observation_space.shape[0], env.action_space.n])
print(Q.shape)
# 2. Parameters of Q-learning
eta = .628
gma = .9
epis = 5000
rev_list = []  # rewards per episode calculate
# 3. Q-learning Algorithm
for i in tqdm(range(epis)):
    # Reset environment
    s = env.reset()
    rAll = 0
    d = False
    j = 0
    # The Q-Table learning algorithm
    while j < 99:
        # env.render()
        j += 1
        # Choose action from Q table
        a = np.argmax(Q[s, :] + np.random.randn(1, env.action_space.n) * (1. / (i + 1)))
        a = np.clip(a, 0, 15)
        # Get new state & reward from environment
        s1, r, d, _ = env.step(a)
        # Update Q-Table with new knowledge
        Q[s, a] = Q[s, a] + eta * (r + gma * np.max(Q[s1, :]) - Q[s, a])
        rAll += r
        s = s1
        if d == True:
            break
    rev_list.append(rAll)
    # env.render()
print("Reward Sum on all episodes " + str(sum(rev_list) / epis))
print("Final Values Q-Table")
print(Q)

