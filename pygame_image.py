import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))#練習1
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img1 = pg.transform.flip(bg_img,True,False)#練習7
    kk_img = pg.image.load("fig/3.png")#練習2
    kk_img = pg.transform.flip(kk_img,True,False)#練習2
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)#練習2
    kk_rct = kk_img.get_rect()#練習8
    kk_rct.center = 300,200#練習8
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()#練習８：キーの押下状態を取得
        if key_lst[pg.K_UP]:#練習８：上矢印のとき
            kk_rct.move_ip((0,-1))#練習８：縦座標を-1
        if key_lst[pg.K_DOWN]:#練習８：下矢印のとき
            kk_rct.move_ip((0,+1))#練習８：縦座標を+1
        if key_lst[pg.K_RIGHT]:#練習８：右矢印のとき
            kk_rct.move_ip((+1,0))#練習８：横座標を+1
        if key_lst[pg.K_LEFT]:#練習８：左矢印のとき
            kk_rct.move_ip((-1,0))#練習８：横座標を-1
        x = -(tmr%3200)#練習6#練習7
        screen.blit(bg_img, [x, 0])#練習3#練習6
        screen.blit(bg_img1, [x+1600, 0])#練習7
        screen.blit(bg_img, [x+3200, 0])#練習3#練習7
        screen.blit(bg_img1, [x+4800, 0])#練習3#練習7
        screen.blit(kk_img, kk_rct)#練習4#練習8
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()