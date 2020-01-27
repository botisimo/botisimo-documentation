:orphan:

Default EJS Template for Queue Overlay
======================================

::

    queue = {
        enabled: boolean;     // If true then the queue is enabled
        prefix: string;       // The command prefix for the account
        current: Array<{
            name: string;     // The name of the user in the queue
            message?: string; // The message attached to the user in the queue
        }>;
        next: Array<{
            name: string;     // The name of the user in the queue
            message?: string; // The message attached to the user in the queue
        }>;
    }

::

    <% if (queue.enabled) { %>
        <div class="flex-none instructions">
            <span class="text">
                <span>
                    type "<strong><%= queue.prefix %>queue join</strong>" in chat to enter the queue
                </span>
            </span>
        </div>
    <% } %>
    <div class="column scroll hide-scrollbar queue">
        <% if (queue.current.length > 0) { %><h3>CURRENT</h3><% } %>
            <% let i = 0; for (const queueItem of queue.current) { i++; %>
            <div class="message">
                <span class="text">
                    <%= queueItem.name %>
                    <%= queueItem.message ? ` - ${queueItem.message}` : '' %>
                </span>
            </div>
        <% } %>
        <% if (queue.next.length > 0) { %><h3>QUEUE</h3><% } %>
        <% i = 0; for (const queueItem of queue.next) { i++; %>
            <div class="message">
                <span class="name"><%= i + 1 %>.</span>
                <span class="text">
                    <%= queueItem.name %>
                    <%= queueItem.message ? ` - ${queueItem.message}` : '' %>
                </span>
            </div>
        <% } %>
    </div>
