# 74. Claude Code in action

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287805
**Section:** 10 Anthropic Apps

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Claude Code in action
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Claude Code isn't just a tool for writing code - it's designed to work alongside you throughout every phase of a software project. Think of it as another engineer on your team who can handle everything from initial setup to deployment and support.

The /init Command

When you start working with Claude Code on a project, the first thing you'll want to do is run the /init command. This tells Claude to scan your entire codebase and understand your project's structure, dependencies, coding style, and architecture.

Claude summarizes everything it learns in a special file called CLAUDE.md. This file automatically gets included as context in all future conversations, so Claude remembers important details about your project.

You can have multiple CLAUDE.md files for different scopes:

Project - Shared between all engineers working on the project
Local - Your personal notes that aren't checked into git
User - Used across all your projects

When running /init, you can add special directions for areas you want Claude to focus on. The generated file will include build commands, coding guidelines, and project-specific patterns that Claude should follow.

You can also quickly add notes to your CLAUDE.md file using the # command. For example, typing # Always use descriptive variable names will prompt you to add this guideline to your project, local, or user memory.

Common Workflows

Claude works best when you approach it as an effort multiplier. The more context and structure you provide, the better results you'll get. Here's the most effective workflow:

Step 1: Feed Context into Claude
Before asking Claude to build something, identify files in your codebase that are relevant to the feature you want to create. Ask Claude to read and analyze these files first. This gives Claude examples of your coding patterns and existing functionality it can build upon.

Step 2: Tell Claude to Plan a Solution
Instead of jumping straight to implementation, ask Claude to think through the problem and create a plan. Tell Claude specifically not to write any code yet - just focus on the approach and steps needed.

Step 3: Ask Claude to Implement the Solution
Once you have a solid plan, ask Claude to implement it. Claude will write code based on the context and planning work you've already done together.

Test-Driven Development Workflow

For even better results, you can use a test-driven approach:

Feed context into Claude - Same as before, show Claude relevant files
Ask Claude to think of test cases - Have Claude brainstorm what tests would validate your new feature
Ask Claude to implement those tests - Select the most relevant tests and have Claude write them
Ask Claude to write code that passes the tests - Claude will iterate on the implementation until all tests pass

This approach often produces more robust code because Claude has clear success criteria to work toward.

Practical Example

Here's how these workflows look in practice. Let's say you want to add a document conversion tool to an existing project:

// First, ask Claude to read relevant files
> Read the math.py and document.py files

// Then ask for planning (not implementation)
> Plan to implement document_path_to_markdown tool:
1. Create a function that:
   - Takes a file path parameter
   - Validates the file exists  
   - Determines file type from extension
   - Reads binary data from file
   - Leverages existing binary_document_to_markdown function
   - Returns markdown string
2. Add appropriate documentation
3. Register the tool with MCP server
4. Add tests

// Finally, ask for implementation
> Implement the plan

Claude will then create the function, update the necessary files, write tests, and even run the test suite to verify everything works correctly.

Additional Commands

Claude Code include

---

## 🎬 Transcript (English)

To get you some hands-on experience with Claude Code, I created a small project for us to work on. You should find the source for this project in a zip file attached to this lecture. I would encourage you to download this zip, extract its contents, and then start up your code editor inside of this new project directory. I've already opened up the project inside of my editor. And once you have the project open, you might be tempted to look through the project contents and maybe go through a little bit of setup which is described inside the ReadMe file. But before you do, there's something important I would like you to understand about Claude Code. Claude Code is not a tool that is just going to write code for you. Naturally, it absolutely can, but that's not the only thing that Claude Code is about. Instead, you really want to view Claude Code as another engineer who's working on this project alongside you. Every task that you would normally go through on a normal project can really be fully delegated off to Claude. So this includes everything from initially setting up a project to designing new features, to deployment, and to support. As we go through this project, we're going to leverage Claude heavily to aid us in various steps. We will use Claude to set up the project for us, to plan out a new feature, to write tests and code, and then later on, on a slightly different project, I'll show you how we can use Claude Code to automatically discover and fix errors in a production environment. So let's get to it. Back inside my editor, I'm going to open up my terminal and then launch Claude Code inside there by executing Claude. Then once I have this open, I'm going to put in my first directive to Claude. I'm going to ask it to read the contents of the ReadMe file and go through any setup directions that are listed inside of here. I will ask Claude to read the contents of the ReadMe file and execute these setup directions listed in it. Claude will then use a variety of different tools to read that file and then execute a series of different commands. It will create a new virtual environment, activate the environment, and install some dependencies. Once that is complete, we are going to run a command that will help Claude get a better understanding of our project. We're going to do so by running the init command. This is a command that we're going to execute inside of Claude Code itself. When you execute this command, Claude will automatically scan your code base to understand your project's general architecture, coding style, and so on. Once complete, Claude will write all of its findings into a special file named Claude.MD. Whenever we run Claude again in the future, this file will be automatically included as context. And just so you know, there are three different Claude files, Project Local and User. We're going to see some references to these in a minute. So we'll discuss what they're all about then. Whenever you run this init command, you can also actually add in some special directions for some areas for Claude to focus on. So let's try this out right now and see what is generated for our project. I'm going to run the init command, and when I do, I'm going to pass in some special instructions. I'm going to ask Claude to include some detailed notes on defining MCP tools. Once it is all done, I'm going to take a look at the newly generated Claude.MD file. So this is a summary of what Claude thinks of our codebase. At the top, it will list out some important commands that it might need to run in the future. We'll get some listing around our coding style that we've used inside this project. And then as I specially requested, it also included some information around defining MCP tools. As I mentioned a moment ago, this file is going to be included as context for Claude in any follow-up request we make in the future. Now, projects change over time. We might change our coding style or add in some additional commands. So if that ever happens, we can very easily manually edit this file, or we can choose to rerun the init command. If you rerun this command, Claude will update the contents of the Claude MD file. Finally, as a very small shortcut, we can put in a Pound and then type in some specific note that we want to be appended into the contents of that file. So we can use this as a tool to give very specific small directions to Claude that will be included in all follow-up requests. So for me, I might add in a direction here that says something like always apply appropriate types to function args. And if I run that, I'll then be asked where I want to add this little note. This is where we see that Project Local and User memory appear. In my case, this is a note that I want to be shared with everyone who is working on this project, so I will add it to Project memory. Once I add that in, I can then check the contents of my Claude.md file, and either somewhere under Code Style or perhaps at the very bottom, I'll probably see whatever note I just added in. At this point, we have added a new file to our project, and this project is being managed by Git. So normally, we would open up our terminal, stage this new file that we just created into Git, and then commit those changes. We could do all that manually, but it'd be a lot faster if we just asked Claude to do it for us. So I'll ask Claude to stage and commit all changes. Claude will then take a look at all the different changes we have made to the codebase, write a descriptive commit message, and commit those files. Next up, I would like to show you some techniques for increasing Claude's effectiveness when writing code. We are going to add a new feature into this project. As a reminder, this project is a very small, very simple MCP server. We are going to ask Claude to add in a new tool to the server that will read a Word document or a PDF file and convert the contents to Markdown. Now, we absolutely could just type in directions for that to Claude, something like make a Word doc plus PDF file to markdown conversion tool. But before doing that, I want you to know that we can dramatically increase the effectiveness of Claude by putting in a little bit more effort. So let me show you how. Think of Claude Code as being an effort multiplier. If you put a little effort into how you direct Claude, you will get back significantly better results. I'm going to show you two different workflows, two different ways of instructing Claude on how to approach a task. Both of these workflows require a little bit of effort on your side, but they allow Claude to tackle much more complex problems. In this first workflow, we're going to go through three distinct steps. First, we're going to identify some areas of our code base that we know are relevant to a feature that we are trying to work on. We're then going to ask Claude to specifically read and analyze those files. Second, we're going to tell Claude about the feature we want to build and ask it to plan out a solution. So the steps will actually go through to implement whatever feature or problem you're trying to solve. And then finally, after Claude has gone through that planning step, we will ask Claude to actually implement these solutions. Let me show you how we would do this for our particular feature of adding in some new document conversion tool. So first, I'm going to go through my codebase and identify some different relevant files. You'll notice there is a Tools directory, and inside there is a Math.py file. This is an example of a tool that has already been put together. So this might be some file that is relevant for the feature that we are trying to build, just because it gives Claude a better idea of how to author a tool. Second, we might ask Claude to take a look at the document.py file, which includes a very helpful function, binary document to markdown. So this will take in some amount of binary data and convert it to markdown. So we can tell Claude to take a look at these files, and Claude will get a better idea of how to write a tool in the first place, and then how to actually do the conversion. So I'm going to add in some instructions to Claude and ask it to just read the contents of those files. Next, I'm going to ask Claude to plan out the implementation of a new tool called Document Path to Markdown, which will take in a path to a PDF or Word document, read the file, convert the contents to Markdown, and return the results. I'm also going to tell Claude specifically to just plan the feature out and not to write any code just yet. In response, Claude is going to give us a pretty well detailed plan that's going to go through a couple of different steps that will be required to implement this entire thing. Finally, I will ask Claude to implement this plan. It's first going to update the document.py file, which is definitely correct. It's then going to update the main.py file, which is also good. And then finally, it will author a test around this new tool. It's then going to run the test suite and make sure that the test actually passes. You'll notice that in the summary message, Claude also tells me that added in some error handling for non-existent or unsupported file types, which was definitely appropriate, even though it wasn't something that I actually asked for explicitly inside of my description of this feature. I'd like to show you another way that we could have asked Claude to implement this feature. Before I show you this alternative, I'm going to get Claude to remove all the code that it just wrote by stashing these changes. Now I am back to a clean slate where I don't have anything related to that new feature that was just implemented. The second technique that we are going to explore is a test-driven development workflow. Again, this requires some more effort from you up front, but it dramatically increases Claude's effectiveness. With this workflow, we will again ask Claude to take a look at some relevant context. Then, before writing any code, we're going to ask Claude to think of some different tests it could write related to our feature. Next, we will select the most relevant tests and ask Claude to implement them. Finally, after we have got some working tests put together, we will ask Claude to write out a solution and write code until the tests actually pass. So let me show you how this approach would actually look for the same exact feature, one where we are building a tool that's going to read a document off of our hard drive and convert its contents into Markdown. First, I'm going to run the slash clear command. This is going to clear up my conversation history with Claude, essentially resetting its context. In this case, I'm doing this just so it doesn't cheat off its previous solution. Then I will ask Claude to read those two relevant files once again. Then I'm going to add in some very clear instructions to think of some tests that it might write to evaluate this new feature that we want to build. Again, I'm going to ask it specifically to not write any code just yet. The suggestions I get back are really solid. Now, I don't really want to have to worry about tests 6, 7, and 8 because those are a little bit more specialized beyond what we're doing right now. So I'm going to ask Claude to just implement tests one through five. Now we will move on to the last step, where we will ask Claude to write out some code to make these tests pass. Very good, all the tests pass. Now, before we move on, I just want to remind you one more time that Claude Code really is an effort multiplier. You can put in very simple directions, and Claude will do its best. But you can dramatically increase Claude's effectiveness by putting in a little bit of effort on your side as well.

---

## 🎬 トランスクリプト（日本語）

Claude Code の実践的な経験を得るために、 一緒に取り組む小さなプロジェクトを作成しました。このプロジェクトの ソースコードは、この講義に添付されている zip ファイルに入っています。 この zip ファイルをダウンロードして展開し、 この新しいプロジェクトディレクトリ内でコードエディタを起動することを お勧めします。私は既にエディタ内でプロジェクトを開いています。プロジェクトを開いたら、 プロジェクトの内容を調べたり、この講義で説明されている セットアップの一部を行ったりしたくなるかもしれません。 しかし、その前に、 Claude Code について理解してほしい重要なことがあります。 Claude Code は単にコードを生成するツールでは ありません。もちろん、コードを生成することもできますが、それだけではありません。 むしろ、Claude Code はあなたと一緒にこのプロジェクトに取り組む もう一人のエンジニアと考えるべきです。通常のプロジェクトで 行うあらゆるタスクは、Claude に委任することができます。 これには、プロジェクトの初期セットアップから、 新機能の設計、デプロイ、サポートまで、すべてが含まれます。 このプロジェクトを進めるにあたり、私たちは様々なステップで Claude を活用していきます。Claude を使ってプロジェクトをセットアップし、 新機能の計画を立て、テストとコードを記述します。そして後ほど、 少し異なるプロジェクトで、Claude Code を使用して 本番環境のエラーを自動的に検出し修正する方法を示します。 早速始めましょう。エディタに戻り、ターミナルを開いて、 そこで Claude を起動します。Claude と入力して実行します。 そうすると、Claude が起動します。 これで開けたら、Claude への最初の指示を入力します。 ReadMe ファイルの内容を読み込み、 その中に記載されているセットアップ手順を実行するように指示します。 ReadMe ファイルの内容を読み込み、そこに記載されている セットアップ手順を実行するように Claude に依頼します。 Claude は様々なツールを使用してファイルを読み取り、 一連のコマンドを実行します。新しい仮想環境を作成し、 環境をアクティベートして、いくつかの依存関係をインストールします。 それが完了したら、 Claude がプロジェクトをよりよく理解するのに役立つコマンドを実行します。 init コマンドを実行します。これは Claude Code 内で実行するコマンドです。 このコマンドを実行すると、 Claude はコードベースを自動的にスキャンして、 プロジェクトの全体的なアーキテクチャ、コーディングスタイルなどを理解します。 完了すると、Claude はそのすべての発見事項を Claude.MD という特別なファイルに書き込みます。 将来 Claude を再び実行する際には、このファイルが 自動的にコンテキストとして含まれます。そして、 ご理解いただくために、Claude には Project、Local、User の 3 つの異なる Claude ファイルがあります。これらへの参照がすぐに表示されますので、 その時点ではそれらがどのようなものかについて説明します。この init コマンドを実行する際には、 Claude に集中してほしい領域の特別な指示を 追加することもできます。それでは、実際に試してみて、 私たちのプロジェクトのために何が生成されるか見てみましょう。init コマンドを実行します。 実行時に、いくつかの特別な指示を渡します。 MCP ツールの定義に関する詳細なメモを含めるように Claude に依頼します。 完了したら、新しく生成された Claude.MD ファイルを確認します。 これは Claude が私たちのコードベースについてどのように考えているかの概要です。 上部には、将来実行する必要がある可能性のある重要なコマンドがいくつかリストアップされます。 プロジェクトで使用されているコーディングスタイルに関するリストも表示されます。 そして、特別に要求したように、MCP ツールの定義に関する情報も含まれています。 先ほども述べたように、このファイルは、 将来行うすべてのリクエストのコンテキストとして含まれます。 プロジェクトは時間とともに変化します。コーディングスタイルを変更したり、 追加のコマンドを追加したりするかもしれません。もしそうなった場合は、 このファイルを簡単に手動で編集するか、init コマンドを再実行することを選択できます。 このコマンドを再実行すると、Claude は Claude.MD ファイルの内容を更新します。 最後に、非常に簡単なショートカットとして、 ハッシュ記号を入力し、そのファイルの内容に追加したい 特定のメモを入力することができます。このようにして、 Claude への非常に具体的で短い指示を与えるツールとして使用でき、 これらはすべての後続のリクエストに含まれます。 私の場合、例えば「常に適切な型を関数引数に適用してください」のような指示を 追加することがあります。 それを実行すると、この小さなメモをどこに追加したいか尋ねられます。 ここで Project、Local、User メモリが表示されます。 私の場合は、このプロジェクトで作業するすべての人と共有したいメモなので、 Project メモリに追加します。 それを追加したら、Claude.md ファイルの内容を確認できます。 コードスタイルに関するセクションか、あるいは一番下あたりに、 追加したメモが見つかるはずです。この時点で、 プロジェクトに新しいファイルを追加しました。そしてこのプロジェクトは Git で管理されています。 通常であれば、ターミナルを開き、 作成したばかりの新しいファイルを Git にステージングし、 その変更をコミットします。すべて手動で行うこともできますが、 Claude に依頼する方がはるかに速いです。 そこで、Claude にすべての変更をステージングしてコミットするように依頼します。 Claude は、コードベースに加えられたすべての変更を確認し、 説明的なコミットメッセージを記述して、 それらのファイルをコミットします。次に、 コードを書く際に Claude の効果を高めるためのテクニックをいくつか紹介します。 このプロジェクトに新しい機能を追加します。 念のためですが、このプロジェクトは非常に小さく、非常にシンプルな MCP サーバーです。 このサーバーに新しいツールを追加するように Claude に依頼します。 このツールは Word 文書または PDF ファイルを読み取り、 その内容を Markdown に変換します。 Word 文書と PDF ファイルから Markdown への変換ツールを作成してほしい、 といった指示を Claude に入力することもできます。しかし、 そうする前に、より多くの労力をかけることで、 Claude の効果を劇的に向上させることができることを知っておいてほしいです。 どのように行うかお見せします。 Claude Code を労力乗数と考えてください。 Claude への指示の仕方で少し労力をかけると、 より良い結果が得られます。 Claude にタスクのアプローチを指示する 2 つのワークフロー、2 つの方法を示します。 どちらのワークフローも、あなたの方で少しの労力が必要ですが、 より複雑な問題を Claude に解決させることができます。 この最初のワークフローでは、3 つの異なるステップを実行します。 まず、取り組もうとしている機能に関連していることがわかっている コードベースの領域を特定します。次に、 Claude にそれらのファイルを特定して分析するように依頼します。 第二に、Claude に作りたい機能について伝え、 ソリューションの計画を立てるように依頼します。つまり、 機能や問題を解決するために実際に行う手順です。そして最後に、 Claude が計画ステップを完了したら、 Claude にこれらのソリューションを実際に実装するように依頼します。 新しいドキュメント変換ツールを追加するという、私たちの特定の機能について、 どのように行うかお見せします。 まず、コードベースを調べ、関連するいくつかのファイルを見つけます。 Tools ディレクトリがあり、その中に Math.py ファイルがあります。 これは既に作成されたツールの例です。 これは、作成しようとしている機能に関連するファイルかもしれません。 単に Claude にツールの作成方法のアイデアを与えるためです。 第二に、document.py ファイルに注目するように Claude に依頼するかもしれません。 このファイルには、非常に役立つ関数、 バイナリドキュメントからマークダウンへの変換機能が含まれています。 これは、ある程度のバイナリデータを取得してマークダウンに変換します。 それで、Claude にこれらのファイルを見るように指示すると、 Claude はまずツールの書き方、次に変換の実行方法について、 より良いアイデアを得ることができます。 そこで、Claude に指示を追加し、 それらのファイルのコンテンツを読むように依頼します。 次に、Document Path to Markdown と呼ばれる新しいツールの実装計画を Claude に立てるように依頼します。このツールは、PDF または Word 文書へのパスを受け取り、 ファイルを読み取り、コンテンツを Markdown に変換し、 結果を返します。また、Claude に specifically 指示します。単に機能を計画するように、コードはまだ書かないでください。 応答として、Claude は非常に詳細な計画を提供します。 この機能全体を実装するために必要ないくつかの異なるステップが含まれています。 最後に、Claude にこの計画を実装するように依頼します。 最初に document.py ファイルを更新します。これは確かに正しいです。 次に main.py ファイルを更新します。これも良いです。 そして最後に、この新しいツールに関するテストを作成します。 その後、テストスイートを実行し、テストが実際に パスすることを確認します。サマリーメッセージで、 Claude は、存在しない、またはサポートされていないファイルタイプに対する エラー処理を追加したとも述べています。これは間違いなく適切でした。 機能の説明に具体的に要求されていなかったにもかかわらず。 この機能も実装するために、Claude に依頼できる別の方法を示したいと思います。 この代替案を示す前に、Claude に これらの変更をスタッシュすることで、 それが書いたコードをすべて削除させます。 これで、先ほど実装された新しい機能に関連するものがなくなった、 クリーンな状態に戻りました。 次に探求する 2 つ目のテクニックは、テスト駆動開発ワークフローです。 これも最初にあなたからの労力がより多く必要ですが、 Claude の効果を劇的に向上させます。このワークフローでは、 Claude に関連するコンテキストをいくつか確認するように再び依頼します。 次に、コードを書く前に、 Claude に機能に関連するいくつかの異なるテストを考えるように依頼します。 次に、最も関連性の高いテストを選択し、 Claude にそれらを実装するように依頼します。最後に、 いくつかの有効なテストを作成したら、 Claude にソリューションを作成し、テストが実際にパスするまでコードを書くように依頼します。 このアプローチが実際にどのように見えるか、同じ機能で 示しましょう。ドキュメントをハードドライブから読み取り、 その内容を Markdown に変換するツールを構築する機能です。 まず、クリアコマンドを実行します。 これは Claude との会話履歴をクリアし、コンテキストをリセットします。 この場合、前のソリューションからカンニングしないように行っています。次に、 2 つの関連ファイルを再度確認するように Claude に依頼します。 次に、ビルドしたい新しい機能を評価するために 作成できるいくつかのテストについて考えるように、 非常に明確な指示を入力します。もう一度、まだコードを書かないように 依頼します。返ってくる提案は非常に堅実です。 次に、テスト 6、7、8 については、 これらは現在行っていることより少し特殊なので、気にしたくありません。 したがって、Claude にテスト 1 から 5 までを実装するように依頼します。 次に、最後のステップに進み、Claude にこれらのテストをパスさせるためのコードを書くように依頼します。 すべてのテストがパスしました。次に、 次に進む前に、Claude Code が本当に 労力乗数であることをもう一度思い出してください。 非常に簡単な指示を与えることができます。Claude は最善を尽くします。しかし、 あなたの方でも少し労力をかけることで、Claude の効果を劇的に高めることができます。
