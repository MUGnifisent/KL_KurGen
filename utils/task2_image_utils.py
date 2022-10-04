from PIL import Image, ImageDraw, ImageFont
from utils.colors import colors
 

# name : (row, col)
karnaugh_matrix_A_truth = {
    '0': (0, 0),  '1': (0, 1),  '3': (0, 2),  '2': (0, 3),
    '4': (1, 0),  '5': (1, 1),  '7': (1, 2),  '6': (1, 3),
    'C': (2, 0),  'D': (2, 1),  'F': (2, 2),  'E': (2, 3),
    '8': (3, 0),  '9': (3, 1),  'B': (3, 2),  'A': (3, 3)
}
karnaugh_matrix_B_truth = {
    '10': (0, 0),  '11': (0, 1),  '13': (0, 2),  '12': (0, 3),
    '14': (1, 0),  '15': (1, 1),  '17': (1, 2),  '16': (1, 3),
    '1C': (2, 0),  '1D': (2, 1),  '1F': (2, 2),  '1E': (2, 3),
    '18': (3, 0),  '19': (3, 1),  '1B': (3, 2),  '1A': (3, 3)
}


# Image setup
WIDTH = 1600
HEIGHT = 1000
CELL_SIZE = 150
MATRIX_A_POS = (100, 200)
MATRIX_B_POS = (900, 200)
MAX_ROW = 3
MAX_COL = 3


class CellGroup:
    def __init__(self, cells, min_cell, max_cell):
        self.cells = cells
        self.min_cell = min_cell
        self.max_cell = max_cell
        self.sticks_left = False
        self.sticks_right = False
        self.sticks_top = False
        self.sticks_bottom = False


def getCellPos(cell, matrix_key = ''):
    # Check if it's A or B matrix
    if isinstance(cell, str):
        if len(cell) == 1:
            row = karnaugh_matrix_A_truth[cell][0]
            col = karnaugh_matrix_A_truth[cell][1]
            matrix_pos = MATRIX_A_POS
        else:
            row = karnaugh_matrix_B_truth[cell][0]
            col = karnaugh_matrix_B_truth[cell][1]
            matrix_pos = MATRIX_B_POS
    elif isinstance(cell, tuple):
        row, col = cell
        if matrix_key.lower() == 'a':
            matrix_pos = MATRIX_A_POS
        elif matrix_key.lower() == 'b':
            matrix_pos = MATRIX_B_POS
    return (matrix_pos[0] + (CELL_SIZE / 2) + (col * CELL_SIZE), matrix_pos[1] + (CELL_SIZE / 2) + (row * CELL_SIZE))


def maxCell(cells):
    cell = max(cells, key = lambda c: c[0] + c[1])
    return cell


def minCell(cells):
    cell = min(cells, key = lambda c: c[0] + c[1])
    return cell


def checkCell(cell, lost_cells, found_cells):
    if cell not in found_cells:
        try:
            i = lost_cells.index(cell)
            lost_cells.pop(i)
            return True  # It's our cell! 
        except ValueError:
            return False  # Not in list


def drawOutline(image_draw, color, cells, cell_repetitions):
    outline_size = 10  # Start width, height of rect
    thickness = 4  # Rect outline thikness
    offset = thickness + 4  # Start offset to avoid rects overlapping
    radius = 8  # Corner radius
    trans_offset = CELL_SIZE / 1.5  # Offset out of matrix for "teleportation"

    matrix_cells = {'a': [], 'b': []}

    print("cells: ", cells)

    # Convert cell names to cell indeces (row, column)
    for cell_name in cells:
        if len(cell_name) == 1:
            matrix_cells['a'].append(karnaugh_matrix_A_truth[cell_name])
        else:
            matrix_cells['b'].append(karnaugh_matrix_B_truth[cell_name])
        if cell_name in cell_repetitions:
            cell_repetitions[cell_name] += 1
        else:
            cell_repetitions[cell_name] = 0

    for matrix_key in matrix_cells:
        cells_in_group = len(matrix_cells[matrix_key])
        max_repetitions = cell_repetitions[max(cell_repetitions, key = lambda k: cell_repetitions[k])]

        if cells_in_group == 1:
            cell_pos = getCellPos(cells[0])
            image_draw.rounded_rectangle(
            [
                cell_pos[0] - outline_size - (offset * max_repetitions), 
                cell_pos[1] - outline_size - (offset * max_repetitions), 
                cell_pos[0] + outline_size + (offset * max_repetitions), 
                cell_pos[1] + outline_size + (offset * max_repetitions)
            ], radius = radius, outline = color, width = thickness)

        elif cells_in_group > 1:
            are_together = False
            found_cells_count = 1
            lost_cells = matrix_cells[matrix_key].copy()
            lost_cells.pop(0)
            found_cells = []
            cell_que = []
            cell_que.append(matrix_cells[matrix_key][0])
            found_cells.append(matrix_cells[matrix_key][0])
            # Algorithm to check if cell group is divided into 2 groups 
            # (whether it's a "teleportation")
            while len(cell_que) != 0:
                row = cell_que[0][0]
                col = cell_que[0][1]
                # Check left cell
                check_col = col - 1
                check_row = row
                if check_col >= 0:
                    if checkCell((check_row, check_col), lost_cells, found_cells):
                        found_cells.append((check_row, check_col))
                        cell_que.append((check_row, check_col))
                        found_cells_count += 1
                # Check top cell
                check_row = row - 1
                check_col = col
                if check_row > 0:
                    if checkCell((check_row, check_col), lost_cells, found_cells):
                        found_cells.append((check_row, check_col))
                        cell_que.append((check_row, check_col))
                        found_cells_count += 1
                # Check right cell
                check_col = col + 1
                check_row = row
                if check_col < MAX_COL + 1:
                    if checkCell((check_row, check_col), lost_cells, found_cells):
                        found_cells.append((check_row, check_col))
                        cell_que.append((check_row, check_col))
                        found_cells_count += 1
                # Check bottom cell
                check_row = row + 1
                check_col = col
                if check_row < MAX_ROW + 1:
                    if checkCell((check_row, check_col), lost_cells, found_cells):
                        found_cells.append((check_row, check_col))
                        cell_que.append((check_row, check_col))
                        found_cells_count += 1
                cell_que.pop(0)
            
            if found_cells_count == cells_in_group:
                are_together = True
            else:
                are_together = False
                print("Not together")

            # Not "teleportation"
            if are_together:
                start_cell_pos = getCellPos(minCell(matrix_cells[matrix_key]), matrix_key)
                end_cell_pos = getCellPos(maxCell(matrix_cells[matrix_key]), matrix_key)
                image_draw.rounded_rectangle(
                [
                    start_cell_pos[0] - outline_size - (offset * max_repetitions), 
                    start_cell_pos[1] - outline_size - (offset * max_repetitions), 
                    end_cell_pos[0] + outline_size  + (offset * max_repetitions), 
                    end_cell_pos[1] + outline_size  + (offset * max_repetitions)
                ], radius = radius, outline = color, width = thickness)
            # If "teleportation"
            else:
                Groups = []
                # Check side to which sticks group
                for cells in (found_cells, lost_cells):
                    Cell_Group = CellGroup(cells, minCell(cells), maxCell(cells))
                    if Cell_Group.min_cell[1] == 0:
                        # Left side
                        Cell_Group.sticks_left = True
                    elif Cell_Group.max_cell[1] == MAX_COL:
                        # Right side
                        Cell_Group.sticks_right = True
                    if Cell_Group.max_cell[0] == MAX_ROW:
                        # Bottom side
                        Cell_Group.sticks_bottom = True
                    elif Cell_Group.min_cell[0] == 0:
                        # Top side
                        Cell_Group.sticks_top = True

                    Groups.append(Cell_Group)
                
                for i in range(2):
                    start_cell_pos = getCellPos(Groups[i].min_cell, matrix_key)
                    end_cell_pos = getCellPos(Groups[i].max_cell, matrix_key)
                    xy1 = start_cell_pos
                    xy2 = end_cell_pos
                    if Groups[i].sticks_top and not Groups[i].sticks_bottom:
                        if Groups[abs(i-1)].sticks_bottom:
                            # Top offset
                            xy1 = (start_cell_pos[0] - outline_size - (offset * max_repetitions), 
                                    start_cell_pos[1] - trans_offset)
                            xy2 = (end_cell_pos[0] + outline_size  + (offset * max_repetitions), 
                                    end_cell_pos[1] + outline_size  + (offset * max_repetitions))

                    if Groups[i].sticks_bottom and not Groups[i].sticks_top:
                        if Groups[abs(i-1)].sticks_top:
                            # Bottom offset
                            xy1 = (start_cell_pos[0] - outline_size - (offset * max_repetitions), 
                                    start_cell_pos[1] - outline_size - (offset * max_repetitions))
                            xy2 = (end_cell_pos[0] + outline_size  + (offset * max_repetitions), 
                                    start_cell_pos[1] + trans_offset)

                    if Groups[i].sticks_left and not Groups[i].sticks_right:
                        if Groups[abs(i-1)].sticks_right:
                            # Left offset
                            xy1 = (start_cell_pos[0] - trans_offset, 
                                    start_cell_pos[1] - outline_size - (offset * max_repetitions))
                            xy2 = (end_cell_pos[0] + outline_size  + (offset * max_repetitions), 
                                    end_cell_pos[1] + outline_size  + (offset * max_repetitions))

                    if Groups[i].sticks_right and not Groups[i].sticks_left:
                        if Groups[abs(i-1)].sticks_left:
                            # Right offset
                            xy1 = (start_cell_pos[0] - outline_size - (offset * max_repetitions), 
                                    start_cell_pos[1] - outline_size - (offset * max_repetitions))
                            xy2 = (start_cell_pos[0] + trans_offset, 
                                    end_cell_pos[1] + outline_size  + (offset * max_repetitions))

                    image_draw.rounded_rectangle([xy1[0], xy1[1], xy2[0], xy2[1]], 
                                                radius = radius, outline = color, width = thickness)

        
def fill_karnaugh_map(image_draw, font, truth_table):
    color = '#111122'
    # Fill Karnaugh matrix with values
    cell_start = (MATRIX_A_POS[0]+CELL_SIZE/2, MATRIX_A_POS[1]+CELL_SIZE/2)  # Center of cell [0, 0]
    # Karnaugh matrix A
    for i in range(4*4):
        row = karnaugh_matrix_A_truth[truth_table[i][0]][0]
        col = karnaugh_matrix_A_truth[truth_table[i][0]][1]
        value = truth_table[i][2]
        text_box = image_draw.textbbox((0, 0), value, font = font)
        value_pos = (cell_start[0] + CELL_SIZE * col - text_box[2] / 2, cell_start[1] + CELL_SIZE * row - text_box[3] / 2)
        image_draw.text(value_pos, value, font = font, fill = color)
    # Karnaugh matrix B
    cell_start = (MATRIX_B_POS[0]+CELL_SIZE/2, MATRIX_B_POS[1]+CELL_SIZE/2)
    for i in range(4*4, 4*4*2):
        row = karnaugh_matrix_B_truth[truth_table[i][0]][0]
        col = karnaugh_matrix_B_truth[truth_table[i][0]][1]
        value = truth_table[i][2]
        text_box = image_draw.textbbox((0, 0), value, font = font)
        value_pos = (cell_start[0] + CELL_SIZE * col - text_box[2] / 2, cell_start[1] + CELL_SIZE * row - text_box[3] / 2)
        image_draw.text(value_pos, value, font = font, fill = color)
    

def gen_karnaugh_map_image(truth_table, res, cell_repetitions):

    print(res)

    image = Image.open("media/karnaugh_map.png").copy()
    font = ImageFont.truetype("cambria.ttc", 42)
    image_draw = ImageDraw.Draw(image)

    fill_karnaugh_map(image_draw, font, truth_table)

    i = 0
    for pair in res:
        #print("cells: ", pair[0])
        drawOutline(image_draw, colors[i], pair[0], cell_repetitions)
        i += 1
    
    image.save("output/2.3 (карта Карно).jpg", "JPEG")
