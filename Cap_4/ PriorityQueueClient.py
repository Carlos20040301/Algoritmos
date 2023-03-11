from PriorityQueue import *

queue = PriorityQueue()

for record in [(0, 'Ada'), (1, 'Don'), (2, 'Tim'),
               (0, 'Joe'), (1, 'Len'), (2, 'Sam'),
               (0, 'Meg'), (0, 'Eva'), (1, 'Kai')]:
    queue.insert(*record)

print('After inserting', len(queue),
      'persons on the queue, it contains:\n', queue)

print('Is queue empty?', queue.is_empty())

print('Removing items from the queue:')
while not queue.is_empty():
    print(queue.remove(), end=' ')
    
print()
