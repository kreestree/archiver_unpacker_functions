from unittest import TestCase, main
from main import archiver, unpacker
from typing import NoReturn


class ArchiverTest(TestCase):
    """
    Класс для тестирования функции архивации archiver
    """

    def test_empty_str(self) -> NoReturn:
        """
        Проверка функции на пустое значение
        :return: None
        """

        self.assertEqual(archiver(''), '')

    def test_str_with_digits(self):
        """
        Проверка функции со строкой, содержащей строку. Должно вызываться исключение ValueError.
        :return: None
        """

        with self.assertRaises(ValueError) as e:
            archiver('abccca1')
        self.assertEqual('Строка не должна содержать цифр', e.exception.args[0])

    def test_not_empty_str(self) -> NoReturn:
        """
        Проверка функции с различными данными
        :return: None
        """

        self.assertEqual(archiver('abc'), 'abc')
        self.assertEqual(archiver('aaabbc'), 'a3b2c')
        self.assertEqual(archiver('caabbaaa'), 'ca2b2a3')
        self.assertEqual(archiver('aaaaaaaaaaaa'), 'a12')
        self.assertEqual(archiver('aaaaaaaaaaaaab'), 'a13b')
        self.assertEqual(archiver('caaaaaaaaaaab'), 'ca11b')
        self.assertEqual(archiver('   ...'), ' 3.3')


class UnpackerTest(TestCase):
    """
    Класс для тестирования функции архивации unpacker
    """

    def test_empty_str(self) -> NoReturn:
        """
        Проверка функции на пустое значение
        :return: None
        """

        self.assertEqual(unpacker(''), '')

    def test_not_empty_str(self) -> NoReturn:
        """
        Проверка функции с различными данными
        :return: None
        """

        self.assertEqual(unpacker('a'), 'a')
        self.assertEqual(unpacker('abc'), 'abc')
        self.assertEqual(unpacker('a3b'), 'aaab')
        self.assertEqual(unpacker('a3b2c'), 'aaabbc')
        self.assertEqual(unpacker('ca2b2a3'), 'caabbaaa')
        self.assertEqual(unpacker('a12'), 'aaaaaaaaaaaa')
        self.assertEqual(unpacker('a13b'), 'aaaaaaaaaaaaab')
        self.assertEqual(unpacker('ca11b'), 'caaaaaaaaaaab')
        self.assertEqual(unpacker(' 3.3'), '   ...')


if __name__ == '__main__':
    main()
