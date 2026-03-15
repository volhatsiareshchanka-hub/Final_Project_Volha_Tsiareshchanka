import pytest

pytestmark = [pytest.mark.ui, pytest.mark.inputs]

# TEXT INPUT

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize(
    "text",
    [
        "Playwright",
        "Playwright_123",
        "Test-123",
        "Ab",
        "Valid_text_123",
    ],
    ids=[
        "letters_only",
        "underscore",
        "hyphen",
        "min_length",
        "mixed_valid",
    ],
)
def test_text_input_accepts_valid_values(inputs_page, text):
    inputs_page.open_text_tab()
    inputs_page.submit_value(text)
    inputs_page.check_result_contains(text)


@pytest.mark.positive
def test_text_input_can_submit_by_enter(inputs_page):
    text = "Playwright"
    inputs_page.open_text_tab()
    inputs_page.fill_value(text)
    inputs_page.submit_with_enter()
    inputs_page.check_result_contains(text)


@pytest.mark.negative
def test_text_input_is_required(inputs_page):
    inputs_page.open_text_tab()
    inputs_page.submit_with_enter()

    assert inputs_page.is_value_missing() is True
    assert inputs_page.is_valid() is False
    assert inputs_page.get_validation_message() != ""


@pytest.mark.negative
@pytest.mark.parametrize(
    "text",
    [
        "A",
        "test space",
        "тест",
        "abc@123",
        "!!!",
    ],
    ids=[
        "too_short",
        "space_not_allowed",
        "cyrillic_not_allowed",
        "special_symbols",
        "only_symbols",
    ],
)
def test_text_input_rejects_invalid_values(inputs_page, text):
    inputs_page.open_text_tab()
    inputs_page.submit_value(text)

    assert inputs_page.result_contains_text(text) is False


@pytest.mark.positive
def test_text_result_is_displayed_after_submit(inputs_page):
    text = "Python_123"
    inputs_page.open_text_tab()
    inputs_page.submit_value(text)
    inputs_page.check_result_contains(text)


# EMAIL INPUT

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize(
    "email",
    [
        "test@gmail.com",
        "user_123@yahoo.com",
        "qa-test@company.org",
        "admin@localhost",
    ],
    ids=[
        "gmail",
        "underscore",
        "hyphen_domain",
        "localhost_allowed",
    ],
)
def test_email_input_accepts_valid_emails(inputs_page, email):
    inputs_page.open_email_tab()
    inputs_page.submit_value(email)
    inputs_page.check_result_contains(email)


@pytest.mark.positive
def test_email_input_can_submit_by_enter(inputs_page):
    email = "playwright@test.com"
    inputs_page.open_email_tab()
    inputs_page.fill_value(email)
    inputs_page.submit_with_enter()
    inputs_page.check_result_contains(email)


@pytest.mark.negative
@pytest.mark.parametrize(
    "email",
    [
        "plainaddress",
        "test.com",
        "test@",
        "@gmail.com",
        "test @gmail.com",
    ],
    ids=[
        "no_at_symbol",
        "missing_at",
        "missing_domain",
        "missing_name",
        "space_in_email",
    ],
)
def test_email_input_rejects_invalid_emails(inputs_page, email):
    inputs_page.open_email_tab()
    inputs_page.submit_value(email)

    assert inputs_page.result_contains_text(email) is False


@pytest.mark.positive
def test_email_result_is_displayed_after_submit(inputs_page):
    email = "admin@localhost"
    inputs_page.open_email_tab()
    inputs_page.submit_value(email)
    inputs_page.check_result_contains(email)

# PASSWORD INPUT

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize(
    "password",
    [
        "Test123!",
        "QaPractice1@",
        "Password9#",
    ],
    ids=[
        "basic_valid",
        "mixed_valid",
        "another_valid",
    ],
)
def test_password_input_accepts_valid_passwords(inputs_page, password):
    inputs_page.open_password_tab()
    inputs_page.submit_value(password)
    inputs_page.check_result_contains(password)


@pytest.mark.positive
def test_password_input_can_submit_by_enter(inputs_page):
    password = "Strong123!"
    inputs_page.open_password_tab()
    inputs_page.fill_value(password)
    inputs_page.submit_with_enter()
    inputs_page.check_result_contains(password)


@pytest.mark.negative
@pytest.mark.parametrize(
    "password",
    [
        "Short1!",
        "lowercase1!",
        "UPPERCASE1!",
        "NoDigits!!",
        "NoSpecial123",
    ],
    ids=[
        "less_than_8_chars",
        "no_uppercase",
        "no_lowercase",
        "no_digit",
        "no_special_char",
    ],
)
def test_password_input_rejects_invalid_passwords(inputs_page, password):
    inputs_page.open_password_tab()
    inputs_page.submit_value(password)

    assert inputs_page.result_contains_text(password) is False


@pytest.mark.positive
def test_password_result_is_displayed_after_submit(inputs_page):
    password = "ValidPass1!"
    inputs_page.open_password_tab()
    inputs_page.submit_value(password)
    inputs_page.check_result_contains(password)