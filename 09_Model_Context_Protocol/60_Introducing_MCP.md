# 60. Introducing MCP

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287780
**Section:** 09 Model Context Protocol

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Introducing MCP
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Think of it as a way to shift the burden of tool definitions and execution away from your server to specialized MCP servers.

When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connecting to MCP Servers that contain tools, prompts, and resources. Each MCP server acts as an interface to some outside service.

Understanding MCP Through a Real Example

Let's say you're building a chat interface where users can ask Claude about their GitHub data. A user might ask "What open pull requests are there across all my repositories?" To answer this, Claude needs tools to access GitHub's API.

Without MCP, you'd need to create all the GitHub integration tools yourself. This means writing schemas and functions for every piece of GitHub functionality you want to support.

The Tool Function Problem

GitHub has massive functionality - repositories, pull requests, issues, projects, and much more. To build a complete GitHub chatbot, you'd need to author an incredible number of tools:

Each tool requires both a schema definition and a function implementation. This represents a lot of code that you have to write, test, and maintain as a developer.

How MCP Solves This

MCP shifts the burden of tool definitions and execution from your server to MCP servers. Instead of you writing all those GitHub tools, they're authored and executed inside a dedicated MCP server.

The MCP server acts as a wrapper around GitHub's functionality, providing pre-built tools that you can use without having to implement them yourself.

MCP servers provide access to data or functionality implemented by outside services. They package up complex integrations into reusable components that any application can connect to.

Common Questions About MCP

Who Authors MCP Servers?
Anyone can create an MCP server implementation. Often, service providers themselves will make their own official MCP implementations. For example, AWS might release an official MCP server with tools for their various services.

How is MCP Different from Direct API Calls?
MCP servers provide tool schemas and functions already defined for you. If you call an API directly, you're responsible for authoring those tool definitions yourself. MCP saves you that implementation work.

Isn't MCP Just Tool Use?
This is a common misconception. MCP servers and tool use are complementary but different concepts. MCP is about who does the work of creating and maintaining the tools. With MCP, someone else has already written the tool functions and schemas for you - they're packaged inside the MCP server.

The key insight is that MCP servers provide tool schemas and functions already defined for you, eliminating the need to build and maintain complex integrations yourself.

---

## 🎬 Transcript (English)

In this module, we are going to focus on model context protocol. MCP is a communication layer designed to provide Claude with context and tools without requiring you, the developer, to write a bunch of tedious code. When you first get started with MCP, you will see diagrams that look like this very often. It shows two major elements of MCP, namely the client and the server. The server often contains a number of internal components, named tools, resources, and prompts. And there's a lot of terminology here. So to help you understand all of this, we're going to imagine that we are building a small app and see how MCP fits into it. Our sample app is going to be another chat interface. It's going to allow a user to chat with Claude about their GitHub data. So if a user asks a question like what open pull request do I have across all my different repositories, the expectation is that Claude is probably going to make use of a tool to reach out to GitHub, access the user's account, and see what open pull requests they have, maybe open repositories or whatever else. The point here is that we would implement this probably by using a set of tools. Now, one thing I want to mention really quickly is that GitHub has a tremendous amount of functionality. There are repositories, pull requests, issues, projects, and tons of other things. So to have a complete GitHub chatbot, we would really have to author a tremendous number of tools. If we wanted to build that sample app, we would be on a hook for authoring all these schemas and all these functions. And this is all code that you and I, as developers, would have to write, test, and maintain. That's a lot of effort, a lot of burden being placed on us. This challenge of making developers maintain a big set of integrations is one of the primary difficulties that model context aims to solve. MCP shifts the burden of defining and running tools from your server to something else called an MCP server. So no longer would you and I have to author this tool right here. Instead, it would be authored and executed somewhere else inside of this MCP server. These MCP servers can really be thought of as like an interface to some outside service. So I might have a GitHub MCP server that provides access to data and functionality provided by specifically GitHub, where essentially wrapping up a ton of functionality around GitHub and placing it into this MCP server in the form of a set of tools. So at this point, we have a very basic understanding of what a MCP server is. It gives us access to a set of tools that exposes functionality related to some outside service. And the benefit here is that you and I do not have to author all these different tool schemas and functions and so on. Now that we have this basic understanding, I want to address some very common questions that a lot of people have when they first learn about MCP servers. So, three common questions that seem to always come up. The first common question is, who authors these MCP servers? The answer is anyone. Anyone can make an MCP server implementation. But very often, you'll find that service providers make their own official implementation. So for example, AWS might decide to release their own official MCP server implementation, and inside of it, it might have a wide variety of different tools available for you to use. The second common question is, how is using a MCP server different than just calling a services API directly? Well, as we just saw, if we wanted to call a API directly, such as GitHub, then we would have to author this tool ourselves. And now we can call GitHub directly. So what did we gain here? Well, all that really changed was we are now having to author the schema ourselves and the function implementation ourselves. So simply by adding in the MCP server, we are saving ourselves a little bit time. The final column question is more of a common criticism that you're going to see people have around MCP. And this criticism is most often coming from people who don't quite understand what MCP is all about. So very often, you will see people saying MCP and tool use are the same thing. Well, as I have just laid out to you, MCP servers and tool use, they are complimentary. They are different things, but they are complimentary. The idea behind MCP is that you do not have to author the tool function and the tool schema. That is something is done for you by someone else and is being wrapped up inside of this MCP server. So at some level, yeah, they're kind of similar because we are talking about tool use in both cases, but MCP servers are really talking about who is doing the actual work. So if you ever see this criticism, again, it's usually because people don't quite understand what MCP is all about.

---

## 🎬 トランスクリプト（日本語）

このモジュールでは、モデルコンテキストに焦点を当てます プロトコルです。MCPは通信レイヤーです Claudeにコンテキストとツールを提供するために設計されています 開発者であるあなたが、多くの面倒なコードを書く必要はありません MCPを使い始めると、このような図をよく目にします よく目にします。MCPの2つの主要な要素を示しています すなわち、クライアントとサーバーです。サーバーは しばしば、ツール、リソース、プロンプトと呼ばれる 内部コンポーネントを数多く含んでいます。そして ここに多くの専門用語があります。理解を助けるために 小さなアプリを構築していると想像し、MCPがどのように 適合するかを見ていきましょう 私たちのサンプルアプリは、別のチャットインターフェイスになります ユーザーが自分のGitHubデータについてClaudeとチャットできるようにします ユーザーが「私のすべての異なるリポジトリを横断して、どのようなオープンなプルリクエストがありますか？」のような質問をすると ユーザーが「私のすべての異なるリポジトリを横断して、どのようなオープンなプルリクエストがありますか？」のような質問をすると ユーザーが「私のすべての異なるリポジトリを横断して、どのようなオープンなプルリクエストがありますか？」のような質問をすると ClaudeはおそらくGitHubにアクセスするためにツールを使用するでしょう ClaudeはおそらくGitHubにアクセスするためにツールを使用するでしょう ユーザーのアカウントにアクセスし、どのようなオープンなプルリクエストがあるか、 オープンなリポジトリなどがあるかを確認します ここで言いたいのは、これはツールのセットを使用して実装するだろうということです ここで言いたいのは、これはツールのセットを使用して実装するだろうということです 一つ早く言及しておきたいのは、GitHubには 非常に多くの機能があるということです リポジトリ、プルリクエスト、問題、 プロジェクト、そして他の多くのものがあります 完全なGitHubチャットボットを持つためには、私たちは 膨大な数のツールを記述する必要があります もしそのサンプルアプリを構築したいのであれば、私たちは これらのすべてのスキーマとこれらのすべての関数を記述する責任を負うことになります そして、これはあなたと私が開発者として書く、テストし、維持する必要のあるすべてのコードです そして、これはあなたと私が開発者として書く、テストし、維持する必要のあるすべてのコードです それは多大な労力であり、私たちに多くの負担がかかっています それは多大な労力であり、私たちに多くの負担がかかっています 開発者に大規模な統合セットを維持させるというこの課題は モデルコンテキストが解決しようとしている主な課題の1つです モデルコンテキストが解決しようとしている主な課題の1つです MCPは、ツールの定義と実行の負担を あなたのサーバーから、MCPサーバーと呼ばれる別のものに移します したがって、あなたと私はこのツールを記述する必要はなくなります したがって、あなたと私はこのツールを記述する必要はなくなります 代わりに、それはMCPサーバー内でどこかで記述され、実行されます これらのMCPサーバーは、外部サービスへのインターフェイスと考えることができます これらのMCPサーバーは、外部サービスへのインターフェイスと考えることができます GitHub MCPサーバーは、GitHubが提供するデータと機能へのアクセスを提供している可能性があります GitHub MCPサーバーは、GitHubが提供するデータと機能へのアクセスを提供している可能性があります GitHubの多くの機能をラップし、このMCPサーバーに GitHubの多くの機能をラップし、このMCPサーバーに ツールのセットとして配置しています。したがって、この時点で MCPサーバーが何であるかの基本的な理解ができました それは、外部サービスに関連する機能を提供する一連のツールへのアクセスを提供します それは、外部サービスに関連する機能を提供する一連のツールへのアクセスを提供します そして、ここでの利点は、あなたと私が これらのさまざまなツールスキーマや関数などを記述する必要がないことです これらのさまざまなツールスキーマや関数などを記述する必要がないことです この基本的な理解ができたので、いくつか取り上げたいと思います MCPサーバーについて初めて学ぶ多くの人が持つ一般的な質問 MCPサーバーについて初めて学ぶ多くの人が持つ一般的な質問 常に浮上する3つの一般的な質問です。最初の 一般的な質問は、これらのMCPサーバーは誰が記述しているのですか？ 答えは、誰でもです。誰でもMCPサーバーの実装を作成できます。しかし、多くの場合、サービスプロバイダーが公式の実装を作成します 答えは、誰でもです。誰でもMCPサーバーの実装を作成できます。しかし、多くの場合、サービスプロバイダーが公式の実装を作成します 答えは、誰でもです。誰でもMCPサーバーの実装を作成できます。しかし、多くの場合、サービスプロバイダーが公式の実装を作成します たとえば、AWSは独自の公式MCPサーバー実装をリリースすることを決定し、その中にさまざまなツールを提供している可能性があります たとえば、AWSは独自の公式MCPサーバー実装をリリースすることを決定し、その中にさまざまなツールを提供している可能性があります たとえば、AWSは独自の公式MCPサーバー実装をリリースすることを決定し、その中にさまざまなツールを提供している可能性があります 利用できます。2つ目の一般的な質問は、MCPサーバーを使用することは、サービスのAPIを直接呼び出すこととどう違うのですか？ 利用できます。2つ目の一般的な質問は、MCPサーバーを使用することは、サービスのAPIを直接呼び出すこととどう違うのですか？ 利用できます。2つ目の一般的な質問は、MCPサーバーを使用することは、サービスのAPIを直接呼び出すこととどう違うのですか？ 利用できます。2つ目の一般的な質問は、MCPサーバーを使用することは、サービスのAPIを直接呼び出すこととどう違うのですか？ 先ほど見たように、GitHubのようなAPIを直接呼び出す場合 このツールを自分で記述する必要があります そして今、GitHubを直接呼び出すことができます。それで、ここで何が得られたのでしょうか？ そして今、GitHubを直接呼び出すことができます。それで、ここで何が得られたのでしょうか？ そして今、GitHubを直接呼び出すことができます。それで、ここで何が得られたのでしょうか？ 実際変わったのは、スキーマを自分で記述し、関数を自分で実装する必要があることです スキーマを自分で記述し、関数を自分で実装する必要があることです したがって、MCPサーバーを追加するだけで、時間を少し節約できます。最後の質問 したがって、MCPサーバーを追加するだけで、時間を少し節約できます。最後の質問 したがって、MCPサーバーを追加するだけで、時間を少し節約できます。最後の質問 人々がMCPについて持つ一般的な批判です この批判は、MCPが何であるかをよく理解していない人々から来ることが多いです この批判は、MCPが何であるかをよく理解していない人々から来ることが多いです しばしば、人々はMCPとツール使用は同じものだと言うでしょう。さて、先ほど説明したように しばしば、人々はMCPとツール使用は同じものだと言うでしょう。さて、先ほど説明したように MCPサーバーとツール使用は相補的です。それらは異なるものですが それらは相補的です。MCPの背後にある考え方は ツール関数とツールスキーマを記述する必要がないということです ツール関数とツールスキーマを記述する必要がないということです それは誰かによって行われ、このMCPサーバーにラップされています それは誰かによって行われ、このMCPサーバーにラップされています だから、あるレベルでは、はい 両方ともツール使用について話しているので、似ています 両方ともツール使用について話しているので、似ています しかし、MCPサーバーは実際に実際の作業を行っている主体について話しています ですから、もしあなたがこの批判を見るなら、それは通常、人々がMCPが何であるかをよく理解していないからです ですから、もしあなたがこの批判を見るなら、それは通常、人々がMCPが何であるかをよく理解していないからです
