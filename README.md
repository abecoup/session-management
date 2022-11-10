# session-management

Requirements:
1. Sessions shall expire when the user closes the page.
2. Sessions shall expire when the user closes the tab.
3. Sessions shall expire after one minute of inactivity.
4. Detect when a session expires due to inactivity and display appropriate message to the user.
5. Warn users of a impending session expiry a few minutes before the end of the
inactivity period. Along with the warning, provide users an option to extend their session.
6. The session shall not expire while the user is actively interacting with the
website.
7. Have at least thee types of users (roles). Each group of the users is authorized
to perform certain tasks, that the other ones are not.

## Notes:

When session timer hits 0:
1. logout user, delete session, redirect user to home

Activity defined:
1. (Easy) If a request is made, irrespective of mouse/key events
2. (Mild) If any mouse/key/scroll events are occuring OR a request is made
3. In each case, the session timer should be reset to match SESSION_COOKIE_AGE

In-activity defined:
1. NO mouse/key/scroll events occuring
2. Page not in focus (essentially just NO mouse/key/scroll events occuring)

Potential pseudo-code:

`IF (ANY mouse/key/scroll event occurs) OR (a new request is made): <br>
    session.set_session_timer(settings.SESSION_COOKIE_AGE) <br>
ELSE: <br>
    // they are inactive here <br>
    IF session_timer == 3 minutes (few minutes before expiry): <br>
        alert user, allow extension of session time <br>
        // when this alert is open, mouse/key/scroll events should not influence the session timer.`
        
As a note, we should only be checking for mouse/key/scroll events every so often. It would be ineffecient to be reseting the session timer after EVERY event continously. Could add events as they occur into momentary list, check only every 5-10 seconds to see if its empty. If it is empty, we just continue to let the session timer go down. If it isnt empty, we simply reset the session timer to max again and empty the list. This way we are only ever using a small amount of momentary storage to increase our performance significantly. 
        
