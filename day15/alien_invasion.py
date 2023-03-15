import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # 初始化 Pygame
        pygame.init()

        # 创建游戏设置实例
        self.settings = Settings()

        # 创建一个全屏窗口
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # 将游戏设置中的宽度和高度设置为窗口的实际宽度和高度
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # 设置窗口标题
        pygame.display.set_caption("Alien Invasion")

        # 创建一个存储游戏统计信息的实例，并创建计分板
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # 创建一艘飞船、一个子弹编组和一个外星人编组
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # 创建外星人群
        self._create_fleet()

        # 创建 Play 按钮
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # 检查游戏事件
            self._check_events()

            # 如果游戏处于活动状态，则更新飞船、子弹和外星人
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            # 更新屏幕
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            # 如果用户点击了关闭按钮，则退出游戏
                sys.exit()
            elif event.type == pygame.KEYDOWN:
            # 如果用户按下了键盘，则响应按键事件
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
            # 如果用户松开了键盘，则响应松开事件
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # 如果用户点击了鼠标，则响应鼠标事件
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        # 检查鼠标单击位置是否在 Play 按钮内
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # 如果 Play 按钮被单击且游戏不处于活动状态，则开始新游戏
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()

            # 重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # 删除所有剩余的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一个新的外星人群，并将飞船居中
            self._create_fleet()
            self.ship.center_ship()

            # 隐藏鼠标指针
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """响应按键事件"""
        if event.key == pygame.K_RIGHT:
            # 如果用户按下右箭头键，则将飞船向右移动
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 如果用户按下左箭头键，则将飞船向左移动
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # 如果用户按下 q 键，则退出游戏
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # 如果用户按下空格键，则发射一颗子弹
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            # 如果用户松开右箭头键，则停止向右移动
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # 如果用户松开左箭头键，则停止向左移动
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        # 如果还没有达到子弹限制，则创建一颗新子弹并将其添加到子弹编组中
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # 更新子弹的位置
        self.bullets.update()

        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # 检查子弹与外星人的碰撞
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
          then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            
            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width) # 减去两个外星人的宽度之后，剩余的宽度
        number_aliens_x = available_space_x // (2 * alien_width) # 两个外星人之间的间距为一个外星人的宽度，所以间距为一个外星人的宽度的两倍
        
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            # bullets.sprites()返回一个列表，其中包含编组bullets中的所有精灵
            bullet.draw_bullet()
        self.aliens.draw(self.screen) # draw()自动绘制编组的每个元素

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
