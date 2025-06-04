It looks like it finds the locator correctly, but clicking it doesn't put it in focus. You need to make this work. 

Error:

Locator.click: Timeout 20000ms exceeded.
Call log:
  - waiting for locator("//*[@id=\"react-select-2-input\"]")
    - locator resolved to <input value="" type="text" tabindex="0" autocorrect="off" autocomplete="off" spellcheck="false" autocapitalize="none" aria-autocomplete="list" id="react-select-2-input"/>
  - attempting click action
    2 × waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <div class=" css-1wa3eu0-placeholder">Select Username</div> intercepts pointer events
    - retrying click action
    - waiting 20ms
    2 × waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <div class=" css-1wa3eu0-placeholder">Select Username</div> intercepts pointer events
    - retrying click action
      - waiting 100ms
    38 × waiting for element to be visible, enabled and stable
       - element is visible, enabled and stable
       - scrolling into view if needed
       - done scrolling
       - <div class=" css-1wa3eu0-placeholder">Select Username</div> intercepts pointer events
     - retrying click action
       - waiting 500ms
