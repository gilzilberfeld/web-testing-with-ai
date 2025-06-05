I've got a Stale Element error.

FAILED                      [100%]
S24_tests.py:8 (test_successful_login_selenium)
login_page_selenium = <login_page.LoginPage object at 0x000002438A6B9070>

    def test_successful_login_selenium(login_page_selenium: LoginPage) -> None:
        # Perform login using the Page Object's method
>       login_page_selenium.login("demouser", "testingisfun99")

S24_tests.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
login_page.py:52: in login
    self._select_dropdown_option(self.USERNAME_DROPDOWN_TRIGGER, username)
login_page.py:48: in _select_dropdown_option
    option_element.send_keys(Keys.TAB)
..\..\.venv\Lib\site-packages\selenium\webdriver\remote\webelement.py:305: in send_keys
    self._execute(
..\..\.venv\Lib\site-packages\selenium\webdriver\remote\webelement.py:574: in _execute
    return self._parent.execute(command, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..\..\.venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py:447: in execute
    self.error_handler.check_response(response)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <selenium.webdriver.remote.errorhandler.ErrorHandler object at 0x000002438A6DA090>
response = {'status': 404, 'value': '{"value":{"error":"stale element reference","message":"stale element reference: stale elemen...eptionChain [0x0x7793d09b+107]\\n\\tRtlGetAppContainerNamedObjectPath [0x0x7793d021+561]\\n\\t(No symbol) [0x0]\\n"}}'}

    def check_response(self, response: Dict[str, Any]) -> None:
        """Checks that a JSON response from the WebDriver does not have an
        error.
    
        :Args:
         - response - The JSON response from the WebDriver server as a dictionary
           object.
    
        :Raises: If the response contains an error message.
        """
        status = response.get("status", None)
        if not status or status == ErrorCode.SUCCESS:
            return
        value = None
        message = response.get("message", "")
        screen: str = response.get("screen", "")
        stacktrace = None
        if isinstance(status, int):
            value_json = response.get("value", None)
            if value_json and isinstance(value_json, str):
                import json
    
                try:
                    value = json.loads(value_json)
                    if len(value) == 1:
                        value = value["value"]
                    status = value.get("error", None)
                    if not status:
                        status = value.get("status", ErrorCode.UNKNOWN_ERROR)
                        message = value.get("value") or value.get("message")
                        if not isinstance(message, str):
                            value = message
                            message = message.get("message")
                    else:
                        message = value.get("message", None)
                except ValueError:
                    pass
    
        exception_class: Type[WebDriverException]
        e = ErrorCode()
        error_codes = [item for item in dir(e) if not item.startswith("__")]
        for error_code in error_codes:
            error_info = getattr(ErrorCode, error_code)
            if isinstance(error_info, list) and status in error_info:
                exception_class = getattr(ExceptionMapping, error_code, WebDriverException)
                break
        else:
            exception_class = WebDriverException
    
        if not value:
            value = response["value"]
        if isinstance(value, str):
            raise exception_class(value)
        if message == "" and "message" in value:
            message = value["message"]
    
        screen = None  # type: ignore[assignment]
        if "screen" in value:
            screen = value["screen"]
    
        stacktrace = None
        st_value = value.get("stackTrace") or value.get("stacktrace")
        if st_value:
            if isinstance(st_value, str):
                stacktrace = st_value.split("\n")
            else:
                stacktrace = []
                try:
                    for frame in st_value:
                        line = frame.get("lineNumber", "")
                        file = frame.get("fileName", "<anonymous>")
                        if line:
                            file = f"{file}:{line}"
                        meth = frame.get("methodName", "<anonymous>")
                        if "className" in frame:
                            meth = f"{frame['className']}.{meth}"
                        msg = "    at %s (%s)"
                        msg = msg % (meth, file)
                        stacktrace.append(msg)
                except TypeError:
                    pass
        if exception_class == UnexpectedAlertPresentException:
            alert_text = None
            if "data" in value:
                alert_text = value["data"].get("text")
            elif "alert" in value:
                alert_text = value["alert"].get("text")
            raise exception_class(message, screen, stacktrace, alert_text)  # type: ignore[call-arg]  # mypy is not smart enough here
>       raise exception_class(message, screen, stacktrace)
E       selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found in the current frame
E         (Session info: chrome=137.0.7151.68); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#stale-element-reference-exception
E       Stacktrace:
E       	GetHandleVerifier [0x0x363763+63299]
E       	GetHandleVerifier [0x0x3637a4+63364]
E       	(No symbol) [0x0x191113]
E       	(No symbol) [0x0x197920]
E       	(No symbol) [0x0x199c4a]
E       	(No symbol) [0x0x199cc7]
E       	(No symbol) [0x0x1da51a]
E       	(No symbol) [0x0x1da5a1]
E       	(No symbol) [0x0x1d1fd4]
E       	(No symbol) [0x0x1fe57c]
E       	(No symbol) [0x0x1ceed4]
E       	(No symbol) [0x0x1fe7f4]
E       	(No symbol) [0x0x21fa4a]
E       	(No symbol) [0x0x1fe376]
E       	(No symbol) [0x0x1cd6e0]
E       	(No symbol) [0x0x1ce544]
E       	GetHandleVerifier [0x0x5be033+2531347]
E       	GetHandleVerifier [0x0x5b9332+2511634]
E       	GetHandleVerifier [0x0x389eda+220858]
E       	GetHandleVerifier [0x0x37a528+156936]
E       	GetHandleVerifier [0x0x380c5d+183357]
E       	GetHandleVerifier [0x0x36b6c8+95912]
E       	GetHandleVerifier [0x0x36b870+96336]
E       	GetHandleVerifier [0x0x35664a+9770]
E       	BaseThreadInitThunk [0x0x76a55d49+25]
E       	RtlInitializeExceptionChain [0x0x7793d09b+107]
E       	RtlGetAppContainerNamedObjectPath [0x0x7793d021+561]
E       	(No symbol) [0x0]

..\..\.venv\Lib\site-packages\selenium\webdriver\remote\errorhandler.py:232: StaleElementReferenceException
