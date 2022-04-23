import pygame
from plane_sprites import*

pygame.init()

print("游戏代码。。。")

# 创建时钟对象
clock = pygame.time.Clock()
i = 0  # 记录刷新次数

# 创建屏幕对象
screen = pygame.display.set_mode((480, 700))

# 绘制背景 1.加载 2.blit 绘制 3.update 更新屏幕显示
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄
hero = pygame.image.load("./images/me1.png")
hero_rect = pygame.Rect(190, 530, 102, 126)  # 创建矩形对象（英雄位置，英雄大小）

# 创建敌机精灵
enemy0 = GameSprite("./images/enemy1.png", 1)
enemy1 = GameSprite("./images/enemy1.png", 2)
# 创建组
enemy_group = pygame.sprite.Group(enemy0, enemy1)
# 创建游戏窗口
# 保持窗口enemy = GameSprite("./images/enemy1.png", 1)
while True:

    hero_rect.y -= 1

    #  监听时间
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("游戏退出。。。")

            #  quit 卸载所有模块
            pygame.quit()

            # exit 直接终止当前正在执行的程序
            exit()

    #  修改飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))  # 覆盖上一帧英雄 去掉拖影
    screen.blit(hero, hero_rect)  # 加载 (英雄对象，坐标元组）或(英雄对象，具体对象）

    # 让精灵组调用两个方法
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()  # 所有绘制完成后统一进行帧刷新

    clock.tick(60)  # 指定频率 每秒执行 while true 循环次数 （刷新率）
    i += 1
    print(i)
pass


pygame.quit()