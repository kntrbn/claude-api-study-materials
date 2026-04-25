# 73. Claude Code setup

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287788
**Section:** 10 Anthropic Apps

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Claude Code setup
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Claude Code is a terminal-based coding assistant that runs directly in your command line. Think of it as having Claude available right in your terminal to help with any coding task you're working on.

What Claude Code Can Do

Claude Code comes with a comprehensive set of tools to help with your development workflow:

File operations - Search, read, and edit files in your project
Terminal access - Run commands directly from the conversation
Web access - Search documentation, fetch code examples, and more
MCP Server support - Add additional tools by connecting MCP servers

The MCP integration is particularly powerful because it means you can extend Claude Code's capabilities by adding specialized tools for databases, APIs, or any other services you work with.

Claude Code works across MacOS, Windows WSL, and Linux, so you can use it regardless of your development environment.

Installation

Getting Claude Code set up takes just three steps:

Install Node.js from nodejs.org/en/download (check if you already have it by running npm help in your terminal)
Install Claude Code with the command: npm install -g @anthropic-ai/claude-code
Start and login by running claude in your terminal

When you run the claude command for the first time, it will prompt you to log in to your Anthropic account. The full setup guide is available at docs.anthropic.com if you need more detailed instructions.

Once you're set up, you'll have Claude available directly in your terminal, ready to help with any coding project or task you're working on.

---

## 🎬 Transcript (English)

Let's take a look at Claude Code. We'll do some setup, learn how it works, and see some advanced use cases. Claude Code is a terminal-based coding assistant. This is a program running in your terminal that can help with a wide variety of code-related tasks. To help you with coding projects, Claude Code has access to many different tools. So it has many basic tools like the ability to search, read, and edit files. But it also has many advanced tools like web fetching and terminal access. Finally, Claude Code can act as an MCP client. And you know what that means. It means it can consume tools that are provided by MCP servers. So we can easily expand the capabilities of Claude Code by adding in some additional MCP servers. Let's now go through a little bit of setup and install Claude Code on your machine. Setup is easy. We're going to first install a copy of Node.js. You might already have Node installed on your machine, and to figure out whether or not you do, open up your terminal and execute the command NPM help. If you see a result come back, that means you probably already have Node installed. Once you have node installed, you'll do a NPM install command that will install Claude Code itself. Once installation is complete, run the command Claude at your terminal. This will prompt you to log in to your Anthropic account. Now a full setup guide can be found at the official Anthropic documentation at docs.anthropic.com. Now I'm going to let you go through this setup process on your own, again, just these three steps right here. As soon as you are done, we're going to walk through a little project together and see what Claude Code can really do for us.

---

## 🎬 トランスクリプト（日本語）

Claude Codeを見ていきましょう。セットアップをして、 仕組みを学び、高度なユースケースを見ていきます。 Claude Codeはターミナルベースの コーディングアシスタントです。これは、 ターミナルで実行されるプログラムで、様々なコード関連の タスクを支援できます。コーディングプロジェクトを支援するために、Claude Codeは多くの異なるツールにアクセスできます。 そのため、検索、読み取り、 ファイル編集の機能のような基本的なツールも多くありますが、 Webフェッチやターミナル アクセスのような高度なツールも多くあります。 最後に、Claude CodeはMCPクライアントとして機能できます。 そして、それが何を意味するかはご存知の通りです。MCPによって提供されるツールを 消費できます。 したがって、追加のMCPサーバーをいくつか追加することで、Claude Codeの機能を簡単に拡張できます。 それでは、セットアップを少し進めて、 お使いのマシンにClaude Codeをインストールしましょう。セットアップは 簡単です。まずNode.jsのコピーをインストールします。 お使いのマシンにはすでにNodeがインストールされているかもしれませんが、 それにインストールされているかどうかを確認するには、ターミナルを開き、 NPM helpコマンドを実行してください。結果が返ってくれば、 おそらくすでにNodeがインストールされているということです。 Nodeがインストールされたら、NPM installコマンドを実行して、 Claude Code自体をインストールします。 インストールが完了したら、ターミナルでClaudeコマンドを実行してください。 これにより、Anthropicアカウントへのログインを求められます。 これにより、Anthropicアカウントへのログインを求められます。 完全なセットアップガイドは、公式のAnthropic ドキュメント docs.anthropic.com で確認できます。 この3つのステップを自分でセットアッププロセスを進めてください。 完了したらすぐに、小さなプロジェクトを一緒に見ていきましょう。 Claude Codeが実際に何をしてくれるのか見てみましょう。 Claude Codeが実際に何をしてくれるのか見てみましょう。
