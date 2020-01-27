:orphan:

Default EJS Template for Poll Overlay
=====================================

::

    poll = {
        currencyName: string;     // Name of the currency for the account
        prefix: string;           // The command prefix for the account
        title: string;            // Title of the poll
        closed: boolean;          // If true then users cannot vote in the poll
        pollOptions: Array<{
            key: string;          // The key used to vote on this option
            value: string;        // The name of the option
            percent: number;      // The percent of the total vote this option has
            totalBets: number;    // The total amount that has been bet on this option
            pollVotes: Array<{}>; // Votes cast in this poll
        }>;
        winningOption: {
            key: string;          // The key used to vote on this option
            value: string;        // The name of the option
            percent: number;      // The percent of the total vote this option has
            totalBets: number;    // The total amount that has been bet on this option
            pollVotes: Array<{}>; // Votes cast in this poll
        };
    }

::

    <div class="row flex-none">
        <h4 class="flex"><%= poll.title.toUpperCase() %></h4>
    </div>
    <div class="flex-none">
        <% if (poll.winningOption) { %>
            <h2>
                #<%= poll.winningOption.key%> <%= poll.winningOption.value%> wins!
            </h2>
        <% } %>
    </div>
    <div class="column scroll hide-scrollbar options">
        <% for (option of poll.pollOptions) { %>
            <div class="message">
                <span class="name">
                    <%= option.key %>. <%= option.value %>
                </span>
                <span class="text">
                    <% if (!poll.closed) { %>
                        <span>(type <strong class="success">"<%= poll.prefix %>vote <%= option.key %> [bet]"</strong> in chat to vote)</span>
                    <% } %>
                </span>
            </div>
            <div class="bar">
                <div class="fill" style="width: <%= option.percent %>%"></div>
                <div class="text">
                    <%= option.pollVotes.length %> votes (<%= option.percent %>%) (<%= option.totalBets.toLocaleString() %> <%= poll.currencyName %> bet)
                </div>
            </div>
        <% } %>
    </div>
    <% if (poll.closed) { %>
        <small class="error">voting is closed</small>
    <% } %>
