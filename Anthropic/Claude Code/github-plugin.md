# GitHub Plugin (`github@claude-plugins-official`)

Installed with `claude plugin install github@claude-plugins-official` (or `/plugin install github@claude-plugins-official`). The plugin itself is a thin wrapper that points Claude Code at GitHub's official remote MCP server — it carries no bundled skills or commands of its own, only this manifest and MCP config from [`anthropics/claude-plugins-public`](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/github):

`.claude-plugin/plugin.json`
```json
{
  "name": "github",
  "description": "Official GitHub MCP server for repository management. Create issues, manage pull requests, review code, search repositories, and interact with GitHub's full API directly from Claude Code.",
  "author": {
    "name": "GitHub"
  }
}
```

`.mcp.json`
```json
{
  "github": {
    "type": "http",
    "url": "https://api.githubcopilot.com/mcp/",
    "headers": {
      "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
    }
  }
}
```

Once connected, the remote MCP server (`api.githubcopilot.com/mcp/`) injects its own usage instructions into the session as a `# MCP Server Instructions` block. Captured verbatim from a live session:

> The GitHub MCP Server provides tools to interact with GitHub platform.
>
> Tool selection guidance:
> 1. Use 'list_*' tools for broad, simple retrieval and pagination of all items of a type (e.g., all issues, all PRs, all branches) with basic filtering.
> 2. Use 'search_*' tools for targeted queries with specific criteria, keywords, or complex filters (e.g., issues with certain text, PRs by author, code containing functions).
>
> Context management:
> 1. Use pagination whenever possible with batches of 5-10 items.
> 2. Use minimal_output parameter set to true if the full information is not needed to accomplish a task.
>
> Tool usage guidance:
> 1. For 'search_*' tools: Use separate 'sort' and 'order' parameters if available for sorting results - do not include 'sort:' syntax in query strings. Query strings should contain only search criteria (e.g., 'org:google language:python'), not sorting instructions. Always call 'get_me' first to understand current user permissions and context.
>
> ## Issues
>
> Check 'list_issue_types' first for organizations to use proper issue types. Use 'search_issues' before creating new issues to avoid duplicates. Always set 'state_reason' when closing issues.
>
> ## Pull Requests
>
> PR review workflow: Always use 'pull_request_review_write' with method 'create' to create a pending review, then 'add_comment_to_pending_review' to add comments, and finally 'pull_request_review_write' with method 'submit_pending' to submit the review for complex reviews with line-specific comments.
>
> Before creating a pull request, search for pull request templates in the repository. Template files are called pull_request_template.md or they're located in '.github/PULL_REQUEST_TEMPLATE' directory. Use the template content to structure the PR description and then call create_pull_request tool.

This text is not part of the plugin's own files — it's returned by GitHub's remote MCP endpoint at connection time, so any Claude Code (or other MCP-compatible) client that wires up this same server picks up identical instructions.
