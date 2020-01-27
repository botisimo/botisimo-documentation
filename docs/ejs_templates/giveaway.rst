:orphan:

Default EJS Template for Giveaway Overlay
=========================================

::

    giveaway = {
        currencyName: string;          // Name of the currency for the account
        prefix: string;                // The command prefix for the account
        title: string;                 // Title of the giveaway
        rules?: string;                // Rules of the giveaway
        closed: boolean;               // If true then users cannot enter the giveaway
        cost: number;                  // The cost to enter the giveaway
        allowMultipleEntries: boolean; // If true then users can enter the giveaway multiple times
        maxEntries: number;            // The maximum number of entries per user
        giveawayEntries: Array<{
            username: string;          // The name of the user that entered the giveaway
            winner: boolean;           // If true this user has been selected as a winner
        }>;
        winningEntries: Array<{
            username: string;          // The name of the user that entered the giveaway
            winner: boolean;           // If true this user has been selected as a winner
        }>;
    }

::

    <div class="row flex-none">
        <h4 class="flex"><%= giveaway.title.toUpperCase() %></h4>
    </div>
    <% if (giveaway.rules) { %>
        <div class="flex-none rules">
            <strong>Rules:</strong> <%= giveaway.rules %>
        </div>
    <% } %>
    <div class="flex-none">
        <% for (const entry of giveaway.winningEntries) { %>
            <h2><%= entry.username %> wins!</h2>
        <% } %>
    </div>
    <% if (!giveaway.closed) { %>
        <div class="flex-none instructions">
            <span class="text">
                <span>type <strong class"success">"<%= giveaway.prefix %>enter"</strong> in chat to enter the giveaway</span>
            </span>
            <% if (!giveaway.closed && giveaway.cost > 0) { %>
                <span class="text">
                    <br />
                    cost to enter: <strong><%= giveaway.cost %> <%= giveaway.currencyName %></strong>
                </span>
            <% } %>
            <% if (!giveaway.closed && giveaway.allowMultipleEntries) { %>
                <span class="text">
                    <br />
                    max entries per user: <strong><%= giveaway.maxEntries || 'unlimited' %></strong>
                </span>
            <% } %>
        </div>
    <% } %>
    <div class="column scroll hide-scrollbar entries">
        <% let i = 0; for (const entry of giveaway.giveawayEntries) { i++; %>
            <div class="message">
                <span class="name"><%= i + 1 %>.</span>
                <span class="text">
                    <%= entry.username %> <% if (entry.winner) { %><span class="fa fa-trophy"></span><% } %>
                </span>
            </div>
        <% } %>
    </div>
    <% if (giveaway.closed) { %>
        <small class="error">entry is closed</small>
    <% } %>
