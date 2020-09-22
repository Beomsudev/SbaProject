class Entity:
    def __init__(self, context, fname, train, test, id, label):
        self._context = context # _ 는 default 접근의미, __2개는 private 접근의미
        self._fname = fname
        self._train = train
        self._test = test
        self._id = id
        self._label = label
        # 나머지 완성

    # get, set 만들기
    
    # 위의 내용과 동일 3.7 부터 간소화 됨

    @property
    def context(self) -> str:
        return self._context
    @context.setter
    def context(self,context):
        self._cotext = context

    @property
    def fname(self) -> str:
        return self._fname
    @fname.setter
    def fname(self,fname):
        self._fname = fname

    @property
    def train(self) -> str:
        return self._train
    @train.setter
    def train(self, train):
        self._train = train

    @property
    def test(self) -> str:
        return self._test
    @test.setter
    def test(self, test):
        self._test = test

    @property
    def id(self) -> str:
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def label(self) -> str:
        return self._label
    @label.setter
    def label(self, label):
        self._label = label

    # fname get, set를 만듭니다.

    # train get, set를 만듭니다.

    # test get, set를 만듭니다.

    # id get, set를 만듭니다.

    # label get, set를 만듭니다.
