class Solution:
    def hasCycle(head):
        visited = {}
        temp = head
        while temp:
            if visited[temp] == True:
                return True
            visited[temp] = True
            temp = temp.next
