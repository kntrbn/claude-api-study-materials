# 62. Project setup

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287785
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    2
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Project setup
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                We're going to build a CLI-based chatbot to better understand how MCP clients and servers work together. This hands-on project will give you practical experience with both sides of the MCP architecture.
What We're Building
Our chatbot will allow users to interact with a collection of documents through a command-line interface. The system consists of two main components:

An MCP client that handles user interactions
A custom MCP server that manages document operations

The server will provide two essential tools: one for reading document contents and another for updating them. All documents will be stored in memory for simplicity - no database required.
Important Architecture Note
In real-world projects, you typically implement either an MCP client or an MCP server, not both. You might create:

An MCP server to expose your service to other developers
An MCP client to connect to existing MCP servers

We're building both components in this project purely for educational purposes - to understand how they communicate and work together.
Project Setup
Download the cli_project.zip file attached to this lesson and extract it to your preferred development directory. Open your code editor in the project folder.
The project includes a comprehensive README file with setup instructions. Follow these steps:

Add your Anthropic API key to the .env file
Install dependencies using either UV (recommended) or pip
Run the starter application to verify everything works

Running the Application
Navigate to your project directory in the terminal. You'll see the main project files including main.py, mcp_client.py, and mcp_server.py.
To start the application, use one of these commands:
# If using UV (recommended)
uv run main.py

# If using standard Python
python main.py
When the application starts successfully, you'll see a chat prompt. Test it by asking a simple question like "what's 1+1?" - you should get a quick response from Claude.
With the basic setup complete, we're ready to start implementing MCP features and exploring how clients and servers communicate through the Model Control Protocol.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                cli_project.zip
                                                (opens in new tab)
                                            
                                        
                                    
                                
                                    
                                        
                                            
                                            
                                                cli_project_COMPLETE.zip
                                                (opens in new tab)

---

## 🎬 Transcript (English)

To better understand some aspects of MCP, we are going to start to implement our own CLI-based chatbot. This is going to give us a better idea of how Claude and servers actually work together. In this video, I want to do a little bit of project setup and just help you understand exactly what we're going to make. I've got a lot of project description over here of what we're going to build. We're going to go through all this over time. Right now, I just want you to get a high-level understanding. So as I mentioned, it's going to be a CLI-based chatbot. We're going to allow users to work with a collection of documents. These are going to be fake documents. They're just going to be stored in memory. We're going to build out a small MCP client that is going to connect to our own custom MCP server. For right now, the server is going to have two tools implemented inside of it. One tool to read the contents of a document, and one tool to update the contents of a document. Again, these documents are here on the right-hand side. They're all fake, so they are going to be persisted only in memory. That's it. Now, before we go any further, there is a very important note, something I really want you to understand around this entire process. And that is that on a normal project, typically we would be implementing either a client or an MCP server. So on a real project, we might be authoring just an MCP server to distribute to the world and allow developers to access some service that we have built up. Alternatively, we might be building a project where we make only a MCP client. And the intent here would be that we would be connecting to some outside MCP servers that have already been implemented by some other engineers. So in this project, we are making both a client and a server. And we're just doing that in one project so you get a better understanding of how this stuff actually works together. All right, now that we have this disclaimer out of the way, let's go through just a little bit of setup. Attached to this video, you should find a file named CLIproject.zip inside there is some starter code for our project. Make sure you download that zip file, extract it, and then open up your code editor inside of that project directory. Just to save a little bit of time, I have already done so. So I've already got my code editor open inside of that small project. Inside this project, I would encourage you to take a look at the readme.md file. Inside here, I've placed some setup directions. So it's going to walk you through the process of making sure you put your API key into the .env file inside this project. And it's also going to walk you through the process of installing dependencies, either with uv or without uv. Once you have gone through all this setup, you can then run the starter project right away. To do so inside of your terminal, make sure that you are inside of your project directory. So I called my project MCP. And inside there, I've got all my different project files and folders. To run the project, we will run uv run main.py if you're making use of uv. If you are not making use of uv, then it'll be just python main.py. Now I'm making use of uv. So I'm going to do a uv run main.py. And then when I run that, I should see a chat prompt appear. And if I ask what's one plus one, I should see a response rather quickly. That is it for our setup. So now we can start to focus on adding in some new features to this application.

---

## 🎬 トランスクリプト（日本語）

MCPの側面をより深く理解するために、 独自のCLIベースのチャットボットを実装することから始めます。 これにより、Claudeとサーバーが実際にどのように連携するかについて、 より良い理解が得られます。このビデオでは、 プロジェクトのセットアップを少し行い、 実際に何を作るのかを正確に理解していただくことを目的としています。 構築する内容について、ここに多くのプロジェクトの説明があります。 これらはすべて、時間をかけて見ていきます。現時点では、 全体的な理解を得ていただきたいのです。ですから、 先ほども述べたように、これはCLIベースのチャットボットになります。 ユーザーは文書のコレクションを操作できるようになります。 これらは架空の文書であり、メモリに保存されるだけです。 私たちは、独自のカスタムMCPサーバーに接続する 小さなMCPクライアントを構築します。 現時点では、サーバーには2つのツールが実装されています。 文書の内容を読み取るツールと、 文書の内容を更新するツールです。 繰り返しになりますが、これらの文書は右側にあります。すべて架空なので、 メモリにのみ永続化されます。それだけです。 さて、先に進む前に、非常に重要な注意点があります。 このプロセス全体を通して、皆さんに理解していただきたいこと、 それは、通常のプロジェクトでは、 通常、クライアントまたはMCPサーバーのいずれかを実装します。 つまり、実際のプロジェクトでは、 私たちが構築したサービスに開発者がアクセスできるように、 MCPサーバーを配布するだけかもしれません。 あるいは、MCPクライアントのみを作成するプロジェクトを 構築しているかもしれません。 その意図は、他のエンジニアがすでに実装した 外部のMCPサーバーに接続することです。 したがって、このプロジェクトでは、クライアントとサーバーの両方を作成します。 そして、これは単一のプロジェクトで行っており、 この仕組みがどのように機能するかをより良く理解していただくためです。 さて、この免責事項が済んだので、 少しセットアップを見ていきましょう。 このビデオには、CLIproject.zipというファイルが付随しています。 その中にプロジェクトのスターターコードがあります。 そのzipファイルをダウンロードして展開し、 コードエディタでそのプロジェクトディレクトリを開いてください。 時間を節約するために、私はすでにそうしました。 ですから、すでにコードエディタを開いて、 その小さなプロジェクトの中にいます。 このプロジェクトの中では、readme.mdファイルを 確認することをお勧めします。 ここにセットアップ手順を記載しました。 APIキーをプロジェクト内の.envファイルに 入れる手順を案内します。 また、uvを使用する場合としない場合の依存関係のインストール手順も案内します。 このセットアップがすべて完了したら、 すぐにスタータープロジェクトを実行できます。 そうするには、ターミナル内でプロジェクトディレクトリにいることを確認してください。 私はプロジェクトをMCPと呼びました。 そして、その中にすべてのプロジェクトファイルとフォルダがあります。 プロジェクトを実行するには、 uvを使用している場合は uv run main.py を実行します。 uvを使用していない場合は、単に python main.py です。 私はuvを使用しているので、uv run main.py を実行します。 それを実行すると、チャットプロンプトが表示されるはずです。 そして、What's one plus one?と質問すると、 すぐに応答が見られるはずです。 それでセットアップは完了です。 これで、このアプリケーションに新しい機能を追加することに焦点を当てることができます。
