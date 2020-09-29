:orphan:

Default EJS Template for Events Overlay
=======================================

::

    event = {
        thumbnail?: string; // URL for the thumbnail
        isVideo: boolean;   // If true then the thumbnail url is a video. If false then it is an image
        text: string;       // Text for the event
        subText?: string;   // Subtext for the event
    }

::

    <% if (event) { %>
        <% if (event.thumbnail) { %>
            <% if (event.isVideo) { %>
                <video
                    src="<%= event.thumbnail %>"
                    autoPlay
                    loop
                ></video>
            <% } else { %>
                <img src="<%= event.thumbnail %>" />
            <% } %>
        <% } %>
        <% if (event.text) { %>
            <span class="text">
                <%= event.text %>
            </span>
        <% } %>
        <% if (event.subText) { %>
            <small class="text">
                <%= event.subText %>
            </small>
        <% } %>
    <% } %>
