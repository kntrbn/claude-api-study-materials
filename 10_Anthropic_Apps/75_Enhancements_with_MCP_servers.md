# 75. Enhancements with MCP servers

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287792
**Section:** 10 Anthropic Apps

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Enhancements with MCP servers
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Claude Code has an MCP client built right into it, which means you can connect MCP servers to dramatically expand what Claude can do. This opens up some really powerful possibilities for customizing your development workflow.

How MCP Extends Claude

The Model Context Protocol allows Claude Code to connect to external services and tools through MCP servers. Instead of being limited to Claude's built-in capabilities, you can add custom functionality by connecting servers that provide specific tools, resources, or integrations.

Each MCP server can expose different types of functionality to Claude through three main components: Tools (for taking actions), Prompts (for templates), and Resources (for accessing data).

Setting Up an MCP Server

Adding an MCP server to Claude Code is straightforward. You use the command line to register your server:

claude mcp add [server-name] [command-to-start-server]

For example, if you have a document processing server that starts with uv run main.py, you'd run:

claude mcp add documents uv run main.py

Once registered, Claude Code will automatically connect to your server when it starts up.

Example: Document Processing

A practical example is creating a tool that lets Claude read PDF and Word documents. By building an MCP server with a "document_path_to_markdown" tool, you can ask Claude to convert document contents to markdown format.

When you ask Claude to "Convert the tests/fixtures/mcp_docs.docx file to markdown", it will automatically use your custom tool to read the document and return the converted content.

Popular MCP Integrations

The MCP ecosystem includes servers for many common development tools and services:

sentry-mcp - Automatically discover and fix bugs logged in Sentry
playwright-mcp - Gives Claude browser automation capabilities for testing and troubleshooting
figma-context-mcp - Exposes Figma designs to Claude
mcp-atlassian - Allows Claude to access Confluence and Jira
firecrawl-mcp-server - Adds web scraping capabilities to Claude
slack-mcp - Allows Claude to post messages or reply to specific threads

Building Your Development Workflow

The real power comes from combining multiple MCP servers that match your specific development process. You might set up:

A Sentry server to fetch production error details
A Jira server to read ticket requirements
A Slack server to notify your team when work is complete
Custom servers for your internal tools and APIs

This creates a development environment where Claude can seamlessly work with all the tools and services you already use, making it a much more powerful coding assistant tailored to your specific workflow.

---

## 🎬 Transcript (English)

In this video, I want to show you one of the most interesting aspects of Claude Code. Claude Code has an MCP client embedded inside of it. That means we can connect MCP servers to Claude Code and dramatically expand its functionality. To demonstrate this, we are going to connect Claude Code to the MCP server that we have been working on. We just authored a tool called Document Path to Markdown. We can now expose this tool to Claude Code, allowing it to read the contents of PDF and Word documents. So we are dynamically expanding the capabilities of Claude Code. Let me show you how to set this up. Back inside of my terminal, I'm going to end my running session with a Control-C. I'm then going to add in an MCP server to Claude Code by executing Claude, MCP, add, then we're going to put in the name for our MCP server. Now the name could be anything you want it to be. In our case, we are making a server related to documents, so I'm going to call our server documents. And then finally, we're going to put in the command that we used to start up our server, which for us is uvrun main.py. So uvrun main.py. And that's it. I'm going to execute that, and I'll start Claude Code back up with Claude. And now we can make use of that tool that we just put together to really test it out inside of our test directory. There is a fixtures folder inside there are two demo files, so a Word doc and a PDF doc. Both contain just a tiny bit of documentation around MCP itself. So I'm now going to ask Claude to convert the contents of either one of those files into Markdown. And my expectation is that Claude will make use of that tool that we just authored a moment ago. And if we scroll up just a little bit here, sure enough it worked. So this actually is the contents of that file. This ability to consume MCP servers adds an incredible amount of flexibility to Claude Code, and really opens the door to some really interesting development opportunities. For example, you might decide to add in a series of MCP servers related to your particular development flow. For example, if you use Sentry for production monitoring, you can add a Sentry MCP server to allow Claude to fetch details about errors that are occurring in production. If you make use of JIRA, you can add in an MCP server that will allow Claude to view the contents of specific tickets. If you're a Slack user, you can add Slack to message you whenever Claude is completed working on some particular problem. These are just a small fraction of the possible enhancements that you can add into Claude Code. So it would definitely worth your time to think about how you can enhance your particular development workflow.

---

## 🎬 トランスクリプト（日本語）

このビデオでは、Claude Codeの最も興味深い側面の一つを皆さんにお見せしたいと思います。 Claude CodeにはMCPクライアントが組み込まれています。 これは、MCPサーバーをClaude Codeに接続して、その機能を大幅に拡張できることを意味します。 これを実演するために、私たちが取り組んできたMCPサーバーにClaude Codeを接続します。 私たちは「Document Path to Markdown」というツールを作成しました。 このツールをClaude Codeに公開できるようになり、Claude CodeはPDFやWordドキュメントのコンテンツを読み取ることができます。 つまり、Claude Codeの機能を動的に拡張しているのです。 設定方法を説明します。 ターミナルに戻って、実行中のセッションをControl-Cで終了します。 次にClaude、MCP、addを実行して Claude CodeにMCPサーバーを追加します。 それからMCPサーバーの名前を入力します。 名前は何でも構いません。 今回はドキュメント関連のサーバーを作成するので、サーバー名をdocumentsとします。 そして最後に、サーバー起動に使用するコマンドを入力します。 私たちの場合、それはuvrun main.pyです。 uvrun main.pyです。これで完了です。 実行します。Claudeを再度起動します。 これで、作成したばかりのツールを、テストディレクトリ内で実際に使用できます。 テストディレクトリ内にはfixturesフォルダがあります。 その中に、WordドキュメントとPDFドキュメントのデモファイルが2つあります。 どちらもMCP自体に関する簡単なドキュメントが含まれています。 では、ClaudeにどちらかのファイルのコンテンツをMarkdownに変換するように依頼します。 Claudeが先ほど作成したツールを利用することを期待しています。 そして、ここを少し上にスクロールすると、うまくいったことがわかります。 これは実際にそのファイルのコンテンツです。 MCPサーバーを消費できるこの機能は、Claude Codeに信じられないほどの柔軟性を追加し、本当に興味深い開発機会への扉を開きます。 例えば、開発フローに関連する一連のMCPサーバーを追加することを決定するかもしれません。 例えば、本番環境の監視にSentryを使用している場合、 Sentry MCPサーバーを追加して、Claudeが本番環境で発生しているエラーに関する詳細を取得できるようにすることができます。 JIRAを利用している場合は、Claudeが特定のチケットのコンテンツを表示できるようにするMCPサーバーを追加できます。 Slackユーザーであれば、Claudeが特定の課題の作業を完了したときに、Slackからメッセージを受け取るように追加できます。 これらは、Claude Codeに追加できる可能な拡張機能のほんの一部です。 したがって、独自の開発ワークフローをどのように強化できるかを考える価値は間違いなくあります。 例えば、開発フローに関連する一連のMCPサーバーを追加することを決定するかもしれません。 例えば、本番環境の監視にSentryを使用している場合、 Sentry MCPサーバーを追加して、Claudeが本番環境で発生しているエラーに関する詳細を取得できるようにすることができます。 JIRAを利用している場合は、Claudeが特定のチケットのコンテンツを表示できるようにするMCPサーバーを追加できます。 Slackユーザーであれば、Claudeが特定の課題の作業を完了したときに、Slackからメッセージを受け取るように追加できます。 これらは、Claude Codeに追加できる可能な拡張機能のほんの一部です。 したがって、独自の開発ワークフローをどのように強化できるかを考える価値は間違いなくあります。 例えば、本番環境の監視にSentryを使用している場合、 Sentry MCPサーバーを追加して、Claudeが本番環境で発生しているエラーに関する詳細を取得できるようにすることができます。 JIRAを利用している場合は、Claudeが特定のチケットのコンテンツを表示できるようにするMCPサーバーを追加できます。 Slackユーザーであれば、Claudeが特定の課題の作業を完了したときに、Slackからメッセージを受け取るように追加できます。 これらは、Claude Codeに追加できる可能な拡張機能のほんの一部です。 したがって、独自の開発ワークフローをどのように強化できるかを考える価値は間違いなくあります。 例えば、開発フローに関連する一連のMCPサーバーを追加することを決定するかもしれません。 例えば、本番環境の監視にSentryを使用している場合、 Sentry MCPサーバーを追加して、Claudeが本番環境で発生しているエラーに関する詳細を取得できるようにすることができます。 JIRAを利用している場合は、Claudeが特定のチケットのコンテンツを表示できるようにするMCPサーバーを追加できます。
