import pytest

@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.forms
def test_user_can_fill_and_submit_practice_form(practice_form_page):
    practice_form_page.open()
    practice_form_page.fill_form()
    practice_form_page.submit_form()
    practice_form_page.check_result_visible()

    result = practice_form_page.get_result_text()

    assert "Olga Tsiareshchanka" in result
    assert "volha_tsiareshchanka@gmail.com" in result
    assert "Female" in result
    assert "7277098233" in result
    assert "1989-03-03" in result