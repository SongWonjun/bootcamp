class Song:

  def __init__(self, title):
    self.title = title
    self.next = None
    self.prev = None


class PlayList:
   
  def __init__(self):
    self.head = None
    self.current = None
   
  def show_list(self): # 1. 함수 이름 show_list로 변경, PEP8의 가이드에 따라 함수의 네이밍은 소문자와 단어 사이를 _로 연결해서 작성
    print('\n플레이리스트:')
    node = self.head
    while node: # 2. node의 형태로 간결하게 변경
      print(node.title)
      last = node
      node = node.next

  def add_song(self, new_data): # 3. 함수 이름 add_song, 인자의 네이밍도 new_data로 변경. 
    new_song = Song(new_data) # 4. 변수 이름 new_song으로 변경 

    if self.head is None:
      self.head = new_song
      return
    last = self.head

    while last.next:
      last = last.next

    last.next = new_song
    new_song.prev = last

  def remove_song(self, selection): # 5. 삭제 기능 추가
    pointer = self.head
    while pointer:
        if pointer.title == selection:
            pointer.prev.next = pointer.next
            return
        pointer = pointer.next
    print("노래를 찾을 수 없습니다.\n")

  def play_song(self, selection): # 6. play_song으로 함수 이름 변경
    pointer = self.head
    while pointer is not None: # 7. 가독성 좋은 형태로 변경
      if pointer.title == selection:
        self.current = pointer
        print("Play : %s" % self.current.title)
        return
      pointer = pointer.next
    print("\n노래를 찾을 수 없습니다.")
    return

  def get_prev_song(self): # 8. get_prev_song으로 함수 이름 변경
    if self.current.prev == None: 
      print("앞으로 갈 노래가 없습니다.")
      return
    self.play_song(self.current.prev.title)

list1 = PlayList()
list1.add_song("The Climb")
list1.add_song("Hello")
list1.add_song("Bad Blood")

list1.play_song("Bad Blood")
list1.remove_song("Bad Blood")

list1.play_song("Hello")
list1.get_prev_song()
list1.show_list()
