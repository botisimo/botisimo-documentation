:orphan:

Default EJS Template for Voice Overlay
======================================

::

    speakers = Array<{
        image: string;       // URL to the users thumbnail
        displayName: string; // Name of user speaking
        color: string;       // The color of the user as a hex string (based on Discord role)
    }>

::

    <% speakers.map(speaker => { %>
        <div class="row flex-none message">
            <% if (speaker.image) { %>
                <span class="name">
                    <img class="avatar" src="<%= speaker.image %>" />
                </span>
            <% } %>
            <span class="text" style="color: <%= speaker.color %>;">
                {speaker.displayName}
            </span>
        </div>
    <% } %>
