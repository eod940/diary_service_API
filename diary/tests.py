from django.test import TestCase, Client


# Create your tests here.
class TestOther(TestCase):
    """
    기능 외에 로직을 구현해보는 테스트입니다.
    """
    def setUp(self) -> None:
        self.client = Client()

    def test_validation_password(self):
        """
        주먹구구식으로 password를 검증하는 로직 테스트입니다.
        """
        print("Test 결과")
        password1 = "fdsjf1"
        password2 = "123456"
        password3 = "asdfas"
        password4 = "1fkdl"
        password5 = "asdf"
        password6 = "dgkajsdklgjhae"
        password7 = "asdlfjgasdkgj12345"
        passwordset = [
            password1,
            password2,
            password3,
            password4,
            password5,
            password6,
            password7,
        ]
        if any(char.isdigit() for char in password1):
            print("1. value = ", password1)
        if any(char.isdigit() for char in password2):
            print("2. value = ", password2)
        if any(char.isdigit() for char in password3):
            print("3. value = ", password3)
        print()

        for i in range(len(passwordset)):
            if len(passwordset[i]) >= 6 and any(char.isdigit() for char in passwordset[i]):
                print("success value = ", passwordset[i])
            else:
                print(passwordset[i], "비밀번호는 6글자 이상이어야 하고 그 안에 숫자가 1개 이상들어가야 합니다.")

