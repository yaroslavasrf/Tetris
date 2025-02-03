def check_collision(tetromino, level):
    # Проверяет столкновение тетромино с блоками на уровне
    for block in tetromino.blocks:
        # Если блок выходит за границы или сталкивается с другими блоками
        if block[1] >= 20 or level.grid[block[1]][block[0]]:
            return True
    return False
