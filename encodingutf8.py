import io
import sys

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
