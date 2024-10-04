def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, 0, len(heap) - 1)

def heappop(heap):
    last_elt = heap.pop() 
    if heap:
        return_item = heap[0]
        heap[0] = last_elt
        _siftup(heap, 0) 
        return return_item
    return last_elt

def heapify(x):
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)

def _siftdown(heap, start_pos, pos):
    new_item = heap[pos]
    while pos > start_pos:
        parent_pos = (pos - 1) >> 1
        parent = heap[parent_pos]
        if new_item < parent:
            heap[pos] = parent 
            pos = parent_pos
            continue
        break
    heap[pos] = new_item 

def _siftup(heap, pos):
    end_pos = len(heap)
    start_pos = pos
    new_item = heap[pos]
    child_pos = 2 * pos + 1

    while child_pos < end_pos:
        right_pos = child_pos + 1 
        if right_pos < end_pos and not heap[child_pos] < heap[right_pos]:
            child_pos = right_pos
        heap[pos] = heap[child_pos]
        pos = child_pos
        child_pos = 2 * pos + 1
    heap[pos] = new_item

    _siftdown(heap, start_pos, pos)
