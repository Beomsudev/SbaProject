class Entity:
    def __init__(self, context, fname, train, test, id, label):
        self.context = context # _ 는 default 접근의미, __2개는 private 접근의미
        self.fname = fname
        self.train = train
        self.test = test
        self.id = id
        self.label = label
        # 나머지 완성

    # get, set 만들기
    
    @property
    def context(self) -> str:
        return self._context

    @context
    def context(self, context):
        self._context = context

    # fname get, set를 만듭니다.

    # train get, set를 만듭니다.

    # test get, set를 만듭니다.

    # id get, set를 만듭니다.

    # label get, set를 만듭니다.
