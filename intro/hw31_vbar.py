#2Slay: Michelle Zhu, Linda Zheng
#IntroCS pd03 sec04
#HW31 -- vertical bargraph
#2023-05-01
#time cost: 0.5
#consulted: Andrew Choi

def v_bargraphify(nums):
    height = max(nums)
    graph = ""
    for x in range(height):
        for i in nums:
            if i >= height:
                graph += "x "
            else:
                graph += "  "
        height -= 1
        graph += "\n"
    for i in range(len(nums)):
        graph += str(i) + " "
    print(graph)


x = [0, 1, 2, 3]
v_bargraphify(x)
'''
      *
    * *
  * * *
0 1 2 3
'''

x = [1, 0, 3, 2]
v_bargraphify(x)
'''
    *
    * *
*   * *
0 1 2 3
'''