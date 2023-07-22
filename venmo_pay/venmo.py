from playwright.sync_api import Playwright, sync_playwright, expect
import time

# TODO (vishakh): Remove this during demo
VENMO_HANDLE = "@Suhas-Suresha"
AMOUNT=0.01
PAYMENT_NOTE="Test payment"


def pay_one_time(amount: float, payment_note: str,
                 venmo_handle: str, playwright: Playwright) -> None:

    # TODO: Remove this during demo
    assert amount < 0.05, "Amount must be less than 0.05"

    """Function to pay with Venmo one time"""
    # Load the authentication context for the browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="./auth.json")
    page = context.new_page()
    print("Navigating to Venmo")
    page.goto("https://account.venmo.com/pay")

    # Fill in the payment details
    print("Filling in payment details")
    page.get_by_placeholder("Name, @username, email, phone").click()
    page.get_by_placeholder("Name, @username, email, phone").fill(f"{venmo_handle}")

    # TODO: Find a way to get the Name of the person
    page.get_by_text(f"{venmo_handle}").click()
    page.get_by_test_id("payment-note-input").click()
    page.get_by_test_id("payment-note-input").fill(f"{payment_note}")
    page.get_by_role("button", name="Pay").click()
    page.get_by_placeholder("0").click()
    page.get_by_placeholder("0").fill("0.01")
    page.get_by_role("button", name="Pay").click()

    # NOTE (vishakh). There is another step to confirm the payment. 
    # TODO (vishakh): Remove this sleep during demo
    time.sleep(1000000)

    # ---------------------
    context.close()
    browser.close()

def pay_with_venmo(amount: float, payment_note: str, venmo_handle: str):
    """Function to pay with Venmo"""
    with sync_playwright() as playwright:
        pay_one_time(amount=amount,
                     venmo_handle=venmo_handle,
                     payment_note=payment_note,
                     playwright=playwright)
        
if __name__ == "__main__":
    pay_with_venmo(amount=AMOUNT,
                   payment_note=PAYMENT_NOTE,
                   venmo_handle=VENMO_HANDLE)
