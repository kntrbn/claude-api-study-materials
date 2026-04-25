# 41. The text edit tool

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287760
**Section:** 06 Tool use with Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    The text edit tool
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Important Note: Tool version strings can for all model versions can be found here: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool
Claude comes with one built-in tool that you don't need to create from scratch: the text editor tool. This tool gives Claude the ability to work with files and directories just like you would in a standard text editor.
What the Text Editor Tool Can Do
The text editor tool provides Claude with a comprehensive set of file manipulation capabilities:

View file or directory contents
View specific ranges of lines in a file
Replace text in a file
Create new files
Insert text at specific lines in a file
Undo recent edits to files

This dramatically expands Claude's abilities and essentially gives it the power to act as a software engineer right out of the gate.
Understanding the Implementation Requirements
Here's where things get a bit confusing: while the tool schema is built into Claude, you still need to provide the actual implementation. Think of it this way - Claude knows how to ask for file operations, but you need to write the code that actually performs those operations.

When you use other tools, you write both the JSON schema and the function implementation. With the text editor tool, Claude provides the schema knowledge, but you must write functions to handle Claude's requests to create files, read directories, replace text, and so on.
Schema Versions
While the main schema is built into Claude, you do need to include a small schema stub when making requests. The exact schema depends on which Claude model you're using:
def get_text_edit_schema(model):
    if model.startswith("claude-3-7-sonnet"):
        return {
            "type": "text_editor_20250124",
            "name": "str_replace_editor",
        }
    elif model.startswith("claude-3-5-sonnet"):
        return {
            "type": "text_editor_20241022", 
            "name": "str_replace_editor",
        }

Claude sees this small schema and automatically expands it into the full text editor tool specification behind the scenes.
Practical Example
Let's see the text editor tool in action. When you ask Claude to work with files, it will use the tool to read, modify, and create files as needed.
For example, if you ask Claude to "Open the ./main.py file and summarize its contents", Claude will:

Use the text editor tool to view the file
Read the contents
Provide you with a summary

You can take this further by asking Claude to modify files. For instance: "Open the ./main.py file and write out a function to calculate pi to the 5th digit. Then create a ./test.py file to test your implementation."
Claude will:

View the existing main.py file
Replace its contents with a new implementation including the pi calculation function
Create a new test.py file with appropriate unit tests

Why Use the Text Editor Tool?
You might wonder why this tool exists when modern code editors already have AI assistants built in. The text editor tool becomes valuable in scenarios where:

You're building applications that need to programmatically edit files
You're working in environments without access to full-featured code editors
You want to integrate file editing capabilities directly into your Claude-powered applications

Essentially, the text editor tool lets you replicate much of the functionality of a fancy AI-powered code editor within your own applications, giving you fine-grained control over how Claude interacts with your file system.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
            

---

## 🎬 Transcript (English)

As we saw earlier on inside this module, usually you as developers author all the different tools that we want to pass off to Claude. But there is one tool that Claude has access to by default. This is called the Text Editor tool, and it is built directly into Claude. This tool gives Claude a wide variety of abilities related to just about everything you can do inside of a standard text editor. So for example, this tool gives Claude the ability to open up files or directories and read the contents. It can take a look at specific ranges of text inside of a file. It can add or replace text inside of a file. It can make new files. It can do undo. Essentially, everything you would do inside of a normal text editor. So this dramatically expands Claude's abilities and almost right out of the gate kind of gives Claude the ability to act as a software engineer. Now, understanding the text editor tool is just a little bit confusing, so I want to walk you through a couple of different diagrams and clarify what this tool does for you and what you and I have to do to actually make use of it inside of a project. So the first thing to understand here is that only the JSON schema part is actually built into Claude. And let me clarify what I mean by that. Remember that when we want to make use of tools, we really have to author two separate things. First, on the left hand side, we have to write out that JSON schema spec. This gets provided off to Claude and tells Claude about some tool that it can make use of and all the different arguments that the tool requires. And then on the right-hand side, you and I had to write out a tool function implementation to pair up with that JSON schema. These were actual functions implemented inside of our code base that would be called at some point in time when Claude wanted to use our tool. So we really had to write both sides here. We had to do both the JSON schema and the tool function implementation. So when we make use of the text editor tool, the only thing that is actually kind of provided for us or built into Claude is the JSON schema. That's set of instructions that tells Claude how to make use of this tool. You have to provide an actual implementation to handle all of Claude's requests to use the text editor tool. That does not exist. It is something that you have to write out inside of our codebase. So in other words, whenever Claude decides to say, maybe create a new file, and it sends back a tool use part to us that says, I want to create a new file, we have to provide an actual function that will actually make a new file somewhere on our hard drive. So using the text editor tool is not free, so to speak. It requires a little bit of effort on our side because we have to write out a couple of different functions. Now, let's go over to a Jupyter notebook, and we're going to demo the use of this tool and take a look at how we would write out some of these different functions. Back over here, I'm inside of a new notebook called 005 Text Editor Tool. As usual, you can find this notebook attached to this lecture. Inside this notebook, there's a lot of the exact same helper code that we've been working with so far. But if you take a look at the third cell down, which has a comment at the top of, implementation of the text editor tool, you're going to see that there is a tremendous amount of code inside of here. So this is a class that I put together ahead of time. It contains all the different functions that are required to use the text editor tool. So in other words, this class provides this piece of the puzzle over here. Remember, I just told you a moment ago that we have to write out some code to handle all of the Claude's requests to use the text editor tool. I wrote out that code for you inside of this particular class. Inside of this class, you'll notice that there are some methods, if you scroll down a little bit, like view, which can be used to view the contents of a file or a directory. There is also a string replace function, which will replace a string inside of a file. There is a function to create a file and so on. So everything has already been provided for you inside of this class. I'm going to collapse this cell. And the next thing I want to point out to you is the cell with the comment of make the text edit schema based upon the model version being used. Now, this is where things get just a little bit confusing. So let me very quickly show you a diagram to help you understand what's going on here. Now, I've repeated several times that this text editor tool schema is already built in the Claude, and we do not have to include it. That's kind of mostly true, but also just a little caveat here, just something to make it slightly confusing. When we make our request off to Claude, and we want to make use of this text editor tool, we do need to include a very, very small schema. So we need to send a lot of a schema that's going to look like this right here. The exact type string that we put in here, notice how it has a date, is going to change depending upon the exact version of Claude that we are making use of. So inside this function, I am checking to see if you are making use of Claude 3.7 Sonnet. And if you are, I'm going to return that schema that has a date of that right there. And if you're making use of Claude 3.5, it's going to have a slightly different date. So you are going to have a slightly different date depending upon the exact model version. When we send this very small schema off to Claude, it is going to be automatically expanded into a much, much larger schema. That looks a little something like this. So Claude is going to see that we are including this very small stub schema that has a name of string replace editor. And it's also going to notice the exact type that we are putting right there. Then behind the scenes, we can imagine that this very small schema gets replaced with this much larger one. That lists out a ton of information to Claude on exactly how to use the text editor tool. Now that we have a slightly better idea of what's going on here, I'd like to give you a quick demonstration of what the text editor tool can do. Inside of the same directory as my notebook, I'm going to make a new file called main.py. And inside there, I'm going to make a very simple function called greeting. that will print out hi there, like so. I'll then make sure that I save that file. I'm then going to go back over to my notebook and down at the very bottom, I've added in a cell that's going to add in a empty user message and then send the list messages into run conversation. I'm going to ask Claude to open up the main.py file and just tell me what is inside this file. So I'll ask Claude to open the .slash main.py file and summarize its contents. I'll then run that. And then inside the response, we can see that Claude did, in fact, get the contents of that file. And it's going to be a summary of what's going on inside there. If we take a look at the list of messages, we'll see that we get a tool use block right here, where Claude is asking to view the contents of the main.py file. The code inside of that text editor tool class that I showed you a moment ago is going to receive that command. It's going to open up the file automatically, and then send that contents back over to Claude. We can actually see the contents right here. Now, at this point, you might be kind of curious why the text edit tool exists all. In other words, what does it really do for us? What functionality does it really offer besides the obvious fact that it can somehow work with files on the file system? Well, chances are right now you are making use of a code editor that has a really fancy AI assistant built into it. And you can ask that assistant to refactor files or create files or do whatever else. It turns out that we can largely replicate all the functionality of your fancy code editor by just making use of this text edit tool. So for example, I'm going to update the prompt that I'm sending off to Claude. I'm going to ask Claude to open up that file. and write out a function to calculate pi to the fifth digit. And then after doing so, I'm going to ask Claude to then create a .slash test.py file to test your implementation. I'm going to run this. After the request is complete, I'm going to scroll down to the list of messages that were exchanged. So down here, I've got my initial user message, then our assistant message, in which Claude decides to use the text edit tool, and specifically, it wants to try to view a file. We then send back the contents of that file. Claude then says, OK, great. I know it's inside this file. I'm now going to try to replace its contents by writing in some new content. So we can see right here is the actual implementation of calculating pi. Then if we go a little bit further down, we respond and say that we did the update to the file successfully. Claude is then going to attempt to create the test.py file and write some text into it, specifically some test to test out the implementation it just put together. We can verify that this all happened by taking a look at the newly updated main.py file. So we will now see an implementation for calculating pi, and then an accompanying test.py file as well, where we've got some tests. So once again, using this tool, we can very easily approximate a rather fancy code editor. And you might be thinking, OK, why don't I just use my code editor? Well, there are probably going to be some scenarios on some different applications you might work on, where you might want to edit some files inside of some file system, or something similar, where you don't really have access to a native, full-featured code editor. And this would be a scenario where you would want to make use of the text edit tool.

---

## 🎬 トランスクリプト（日本語）

先ほどこのモジュール内で見たように、通常 開発者である皆さんは、Claudeに渡したい様々なツールをすべて作成します。しかし、一つだけツールがあります Claudeがデフォルトでアクセスできるもの。それは テキストエディタツールと呼ばれ、Claudeに直接組み込まれています。 このツールは、Claudeに 標準的なテキストエディタ内でできることのほとんどすべてに関する、幅広い能力を提供します。 例えば、このツールはClaudeに ファイルやディレクトリを開いて その内容を読み取る能力を与えます。ファイル内の 特定のテキスト範囲を調べたり ファイル内のテキストを追加または置き換えたり 新しいファイルを作成したりできます。元に戻す操作も できます。本質的に、 通常のテキストエディタで行うことはすべて可能です。 これはClaudeの能力を劇的に拡張し ほぼすぐに、ソフトウェアエンジニアとして Claudeに行動させる能力を与えることができます。さて テキストエディタツールの理解は少し 混乱しやすいので、いくつかの異なる図を 通して説明し、このツールが何をするのか そして、プロジェクトで実際に利用するために 皆さんが何をしなければならないのかを 明確にしたいと思います。まず理解すべきことは JSONスキーマ部分のみが Claudeに組み込まれているということです。そして それが何を意味するかを明確にしましょう。 ツールを利用したい場合、実際には2つの 別々のものを作成する必要があることを思い出してください。まず左側には JSONスキーマ仕様を記述する必要があります。これは Claudeに提供され、Claudeに 利用可能なツールとそのツールが必要とするすべての引数について伝えます。 そして右側には、皆さんがツール関数の実装を記述する必要がありました。 これは私たちのコードベース内に実装された 実際の関数であり、Claudeが 私たちのツールを使用したいときに呼び出されます。 そのため、実際には両方の側面を記述する必要がありました。JSON スキーマとツール関数の実装の両方を。 したがって、テキストエディタツールを使用する場合 実際には提供される唯一のものは、JSON スキーマです。それはClaudeに このツールをどのように使用するかを伝える指示セットです。 皆さんは、テキストエディタツールの 使用に関するClaudeのすべてのリクエストを 処理するための実際の実装を提供する必要があります。それは存在しません。 皆さんがコードベース内に記述しなければならないものです。 つまり、Claudeが新しいファイルを作成したいと判断し 私たちにツール使用ブロックを送信する場合 それは新しいファイルを作成したいと言うのですが 私たちは実際にハードドライブのどこかに 新しいファイルを作成する実際の関数を提供する必要があります。 したがって、テキストエディタツールの使用は 文字通りの意味で無料ではありません。私たちの側で 少しの労力を必要とします。なぜなら、いくつかの異なる 関数を記述する必要があるからです。さて、Jupyter Notebookに移り このツールの使用をデモし、これらの異なる 関数をいくつか記述する方法を見ていきましょう。 ここに戻って、新しいノートブックに入ります。 005 Text Editor Tool という名前です。いつものように このノートブックは講義に添付されています。この ノートブック内には、これまで使用してきた ほとんど同じヘルパーコードがあります。しかし、3番目の セルを見ると、「テキストエディタツールの実装」 というコメントがあります。そこには 膨大な量のコードがあることがわかります。これは私が事前にまとめたクラスです。 テキストエディタツールの使用に必要なすべての 異なる関数が含まれています。つまり、このクラスは こちらのパズルのピースを提供します。少し前に説明したように Claudeのリクエストを処理するために コードを記述する必要がありました。私はそのコードを 皆さんのためにこの特定のクラス内に記述しました。このクラス内には いくつかのメソッドがあることに気づくでしょう。少し下にスクロールすると ファイルやディレクトリの内容を表示できる viewというメソッドがあります。また ファイル内の文字列を置換する string replace関数もあります。ファイルを 作成する関数などもあります。したがって、すべてが提供されています。 このクラス内に皆さんのために。このセルを折りたたんで 次に、使用されているモデルバージョンに基づいて テキストエディタのスキーマを作成するという コメントが付いたセルに注目したいと思います。ここで 少し混乱する点があります。なので、ごく簡単に ダイアグラムを見せて、何が起こっているのかを理解するのに役立てます。 さて、このテキストエディタ ツールのスキーマはClaudeにすでに組み込まれており、含める必要はないと何度も申し上げました。 それは大部分真実ですが、 少し注意点もあります。少し混乱させるために。 Claudeにリクエストを送信し、このテキスト エディタツールを利用したい場合、非常に 非常に小さなスキーマを含める必要があります。 なので、多くのスキーマを送信する必要があります。 それはここに表示されているようなものです。日付を 含む文字列の正確なタイプは、 使用しているClaudeの正確なバージョンによって 変わります。ですから、この関数の中では、私は Claude 3.7 Sonnet を使用しているかどうかを確認しています。 そして、使用している場合、そこにある日付の スキーマを返します。そして、Claude 3.5 を 使用している場合、日付が少し異なります。 したがって、正確なモデルバージョンによって 日付が少し異なることになります。そして、この非常に小さな スキーマをClaudeに送信すると、それは 自動的にこのはるかに大きなスキーマに拡張されます。 これはのようなものです。だから、Claudeは 私たちがこの非常に小さな スタブスキーマを含めていることを見て、それは String Replace Editor という名前です。 そして、そこに入れている正確なタイプも認識します。 それから裏側では、この非常に小さな スキーマがこのはるかに大きなものに置き換えられると想像できます。 これはClaudeに、テキストエディタ ツールをどのように使用するかについて 多くの情報を提供します。これで 何が起こっているのかについて、少し良い考えを得られたので テキストエディタツールの 機能の簡単なデモンストレーションを提供したいと思います。 同じディレクトリ内で、私のノートブックの 近くに、main.pyという新しいファイルを作成します。 そしてその中に、greetingという非常に簡単な関数を作成します。 それはこのように「こんにちは」と表示します。 その後、ファイルを保存するようにします。 その後、ノートブックに戻り、下にスクロールして 一番下にあるセルに 空のユーザーメッセージを追加し、メッセージリストを conversation.runに送信するセルを追加しました。 Claudeにmain.pyファイルを開いて このファイルに何が入っているか教えてほしいと頼みます。 したがって、./ main.pyファイルを開いて その内容を要約するようにClaudeに依頼します。 その後実行します。そして レスポンス内で、Claudeが行ったことがわかります。 そしてそれはファイルの内容であり、そこに入っていることの 要約になります。メッセージリストを見ると ツール使用ブロックが表示され、Claudeが main.pyファイルの内容を表示しようとしています。 私が少し前に示したテキストエディタツールクラス内の コードは、そのコマンドを受け取ります。自動的に ファイルを開き、その内容をClaudeに送り返します。 実際の内容はここに表示できます。さて、この時点で、あなたは少し不思議に思っているかもしれません なぜテキスト編集ツールが存在するのかと。つまり、それは ファイルシステムでファイルを操作できるという 明白な事実以外に、他に何をしてくれるのでしょうか？ それは、おそらく今、皆さんは 非常に優れたAIアシスタントを搭載したコードエディタを使用しているでしょう。 そして、そのアシスタントにファイルをリファクタリングしたり、ファイルを作成したり するように依頼できます。それらの機能のほとんどすべてを このテキスト編集ツールを利用するだけで 再現できます。例えば、送信するプロンプトを更新します。 Claudeに。Claudeにファイルを開いて piを小数点以下5桁まで計算する関数を 書き込むように依頼します。その後、Claudeに その実装をテストするための ./test.pyファイルを作成するように依頼します。これを実行します。 完了した後 交換されたメッセージのリストにスクロールします。 ここで、最初のユーザーメッセージ、次に アシスタントメッセージがあり、その中でClaudeが テキスト編集ツールを使用することを決定します。 そして具体的には、ファイルの表示を試みたいようです。 その後、そのファイルの内容を返します。 Claudeは次に、OK、素晴らしい。このファイルに何が入っているか知っています。 私は今、その内容を 新しいコンテンツを書き込むことによって置き換えようとしています。 だから、ここで見ることができるのは piを計算する実際のコードです。 そして、さらに下にスクロールすると、私たちは応答します。 ファイルへの更新を正常に完了したと述べています。 Claudeは次に、test.pyファイルを 作成しようとします。 そして、そこにいくつかのテキストを書き込みます。具体的には すぐに作成した実装をテストするためのものです。 これらすべてが発生したことを検証するには 新しく更新されたmain.pyファイルを見る必要があります。 だから、piを計算するための実装が表示され、 そして、付随するtest.pyファイルも表示されます。そこには テストがあります。したがって、もう一度、この ツールを使用することで、かなり高度な コードエディタを簡単に模倣できます。そして、あなたは 考えているかもしれません。「なぜコードエディタを使わないんだ？」と。 さて、ファイルシステム内の いくつかのファイルを編集したい、あるいは同様の シナリオがあるかもしれません。ネイティブのフル機能の コードエディタにアクセスできない状況では。 そして、これはテキスト編集ツールを使用したいシナリオです。
