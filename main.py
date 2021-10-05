from env import *
from tqdm import tqdm

env = CustomEnv()
env.init_render()
done = False

while not done:
    env.clock.tick(30)
    env.render()
    click = False
    while not click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                click = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                if pygame.mouse.get_pressed(3) == (1, 0, 0):
                    pos = pygame.mouse.get_pos()
                    color = env.window.get_at(pos)[:3]
                    if color != (0, 0, 0):
                        pos_i = pos[0] // 135
                        pos_j = (pos[1] - 200) // 135
                        action = pos_j * 4 + pos_i

                        obs, reward, done, _ = env.step(action)
                        print(obs, reward, done)

pygame.quit()

# # 1. Load Environment and Q-table structure
# env = CustomEnv()
# env.init_render()
# Q = np.zeros([env.observation_space.shape[0], env.action_space.n])
# print(Q.shape)
# # 2. Parameters of Q-learning
# eta = 1.0
# gma = 1.0
# epis = 5000
# rev_list = []  # rewards per episode calculate
# # 3. Q-learning Algorithm
# for i in tqdm(range(epis)):
#     # Reset environment
#     s = env.reset()
#     rAll = 0
#     d = False
#     j = 0
#     # The Q-Table learning algorithm
#     while j < 99:
#         # env.render()
#         j += 1
#         # Choose action from Q table
#         a = np.argmax(Q[s, :] + np.random.randn(1, env.action_space.n) * (1. / (i + 1)))
#         a = np.clip(a, 0, 15)
#         # Get new state & reward from environment
#         s1, r, d, _ = env.step(a)
#         # Update Q-Table with new knowledge
#         Q[s, a] = Q[s, a] + eta * (r + gma * np.max(Q[s1, :]) - Q[s, a])
#         rAll += r
#         s = s1
#         if d == True:
#             break
#     rev_list.append(rAll)
#     # env.render()
# print("Reward Sum on all episodes " + str(sum(rev_list) / epis))
# print("Final Values Q-Table")
# print(Q)
