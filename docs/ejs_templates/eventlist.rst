:orphan:

Default EJS Template for Event List Overlay
===========================================

::

    events = Array<{
        type: string;     // The type of event 'follow' | 'subscription' | 'giftsubscription' | 'donation' | 'bits' | 'raid';
        platform: string; // The platform the event happened on 'discord' | 'facebook' | 'slack' | 'trovo' | 'twitch' | 'youtube';
        data: {
            from: string;     // The username of the viewer who triggered the event
            to: string;       // The name of the channel the event happened
            amount?: number;  // The amount of donations or bits (only available if type is 'bits' or 'donations'
            unit?: string;    // The unit of donations or bits (only available if type is 'bits' or 'donations'
            viewers?: number; // The amount of viewers (only available if type is 'raid')
            plan?: string;    // The subscription plan (only available if type is 'subscription')
        }
    }>

::

    <div className="column scroll hide-scrollbar">
        <% let i = 0; for (const event of events) { i++; %>
            <div className="message">
                <span className="text">
                    <img className="platform-icon" src="/images/<%= event.platform %>-logo-<%= event.platform === 'youtube' ? 'play-' : '' %>drk.png" />
                    <% if (event.type === 'bits' || event.type === 'donation') { %>
                        <%= event.data.from %> donated <% data.amount %><%= data.unit ? ` ${data.unit}` : '' %> to <%= event.data.to %>
                    <% } %>
                    <% if (event.type === 'follow') { %>
                        <%= event.data.from %> donated <% data.amount %>${data.unit ? ` ${data.unit}` : ''} to <%= event.data.to %>
                    <% } %>
                    <%= event.data.from %>
                    <%= event.data.to %>
                    <%= event.data.amount %>
                    <%= event.data.unit %>
                    <%= event.data.viewers %>
                    <%= event.data.plan %>
                </span>
            </div>
        <% } %>
    </div>

switch (type) {
    case CONNECTION_EVENTS.BITS:
    case CONNECTION_EVENTS.DONATION:
      return `donated ${data.amount}${data.unit ? ` ${data.unit}` : ''} to`;
    case CONNECTION_EVENTS.FOLLOW:
      return platform === PLATFORMS.FACEBOOK
        ? 'liked'
        : platform === PLATFORMS.YOUTUBE
        ? 'subscribed to'
        : 'followed';
    case CONNECTION_EVENTS.HOST:
      return 'hosted';
    case CONNECTION_EVENTS.RAID:
      return 'raided';
    case CONNECTION_EVENTS.SUBSCRIPTION:
      return platform === PLATFORMS.YOUTUBE ? 'sponsored' : 'subscribed to';
  }

switch (type) {
    case CONNECTION_EVENTS.BITS:
    case CONNECTION_EVENTS.DONATION:
    case CONNECTION_EVENTS.HOST:
    case CONNECTION_EVENTS.RAID:
      return data.to;
    case CONNECTION_EVENTS.FOLLOW:
      return platform === PLATFORMS.FACEBOOK ? `${data.to}'s video` : data.to;
    case CONNECTION_EVENTS.SUBSCRIPTION:
      return `${data.to}${data.plan ? `with plan ${data.plan}` : ''}`;
  }