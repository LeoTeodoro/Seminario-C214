import unittest
from unittest.mock import MagicMock, patch, Mock

from agenda import Agenda, Show

class AgendaTestMock(unittest.TestCase):

    def test_init(self):
        agenda = Agenda()
        self.assertEqual([], agenda.readShows())

    def test_createShow(self):
        agenda = Agenda()
        show_mock = MagicMock(spec=Show)
        agenda.createShow(show_mock)
        self.assertEqual([show_mock], agenda.readShows())

    @patch('agenda.Agenda.updateShow')
    def test_updateShow_with_patch(self, mock_updateShow):
        agenda = Agenda()
        show_mock = MagicMock(spec=Show)
        agenda.createShow(show_mock)
        updated_show_mock = MagicMock(spec=Show)
        agenda.updateShow(0, updated_show_mock)
        mock_updateShow.assert_called_with(0, updated_show_mock)

    def test_updateShow_with_Mock(self):
        agenda_mock = Mock(spec=Agenda)
        show_mock = Mock(spec=Show)
        agenda_mock.createShow(show_mock)
        updated_show_mock = Mock(spec=Show)
        agenda_mock.updateShow(0, updated_show_mock)
        agenda_mock.updateShow.assert_called_once_with(0, updated_show_mock)

    def test_updateShow_with_MagicMock(self):
        agenda = Agenda()
        show_mock = MagicMock(spec=Show)
        agenda.createShow(show_mock)
        updated_show_mock = MagicMock(spec=Show)
        agenda.updateShow(0, updated_show_mock)
        self.assertEqual([updated_show_mock], agenda.readShows())

if __name__ == '__main__':
    unittest.main()