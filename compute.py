from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

MONITOR_WIDTH = 21.25
MONITOR_HEIGHT = 14.5

NUM_COLORS = 16


def get_code_map(img: Image.Image):
    nimg = np.array(img, dtype=np.uint8)
    nimg = nimg.reshape(-1, 3)
    kmeans = KMeans(n_clusters=NUM_COLORS).fit(nimg)
    labels = kmeans.predict(nimg)
    clusters = kmeans.cluster_centers_.astype(np.uint8)

    return ''.join(map(lambda x: hex(x)[-1], labels)), clusters


def get_code_from_file(file_path: str, num_monitors_wide: int, num_monitors_tall: int) -> str:
    w, h = int(MONITOR_WIDTH * num_monitors_wide) - 6, int(MONITOR_HEIGHT * num_monitors_tall) - 6

    img = Image.open(file_path)
    img = img.resize((w, h)).convert('RGB')

    data, code_map = get_code_map(img)

    code = f"""local monitor = peripheral.find("monitor")
    monitor.setTextScale(0.5)
    local letters = string.rep(" ", {w})
    local letterColors = string.rep("0", {w})
    """

    for i, (r, g, b) in enumerate(code_map):
        code += f'monitor.setPaletteColor({2 ** i}, {hex(int(r) * 256 * 256 + int(g) * 256 + int(b))})\n'

    for i in range(0, len(data), w):
        row = data[i:i + w]
        code += f'monitor.setCursorPos(1, {i // w + 1})\n'
        code += f'monitor.blit(letters, letterColors,"{row}")\n'

    return code
