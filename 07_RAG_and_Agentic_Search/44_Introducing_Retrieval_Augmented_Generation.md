# 44. Introducing Retrieval Augmented Generation

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287763
**Section:** 07 RAG and Agentic Search

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Introducing Retrieval Augmented Generation
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Retrieval Augmented Generation (RAG) is a technique that helps you work with large documents that are too big to fit into a single prompt. Instead of cramming everything into one massive prompt, RAG breaks documents into chunks and only includes the most relevant pieces when answering questions.

The Problem with Large Documents

Imagine you have an 800-page financial document and want to ask Claude specific questions about it, like "What risk factors does this company have?" You need to get the relevant information from the document to Claude somehow, but there are limits to how much text you can include in a prompt.

Option 1: Include Everything in the Prompt

The first approach is straightforward - extract all text from the document and stuff it into your prompt along with the user's question. Your prompt might look like this:

Answer the user's question about the financial document.

<user_question>
{user_question}
</user_question>

<financial_document>
{financial_document}
</financial_document>

This approach has serious limitations:

There's a hard limit on prompt length - your document might be too long
Claude becomes less effective with very long prompts
Larger prompts cost more to process
Larger prompts take longer to process

Option 2: Break Documents into Chunks

RAG takes a smarter approach. First, you break the document into smaller chunks during a preprocessing step. Then, when a user asks a question, you find the chunks most relevant to their question and only include those in your prompt.

Here's how it works: if someone asks "What risks does this company face?" you'd search through your chunks, find the "Risk Factors" section, and include just that relevant chunk in your prompt.

Benefits of RAG

Claude can focus on only the most relevant content
Scales up to very large documents
Works with multiple documents
Smaller prompts cost less and run faster

Challenges with RAG

Requires a preprocessing step to chunk documents
Need a search mechanism to find "relevant" chunks
Included chunks might not contain all the context Claude needs
Many ways to chunk text - which approach is best?

For example, you could split documents into equal-sized portions, or you could create chunks based on document structure like headers and sections. Each approach has trade-offs you'll need to evaluate for your specific use case.

When to Use RAG

RAG involves many technical decisions and requires more work than simply including everything in a prompt. You'll need to analyze whether the benefits outweigh the complexity for your particular application. It's especially valuable when working with very large documents, multiple documents, or when you need to optimize for cost and performance.

The key insight is that RAG trades simplicity for scalability and efficiency. While it requires more upfront work to implement properly, it enables you to work with document collections that would be impossible to handle with simple prompt stuffing.

---

## 🎬 Transcript (English)

In this module, we are going to discuss a tremendous amount about a technique referred to as retrieval augmented generation, or rag for short. In this video in particular, I want to give you a really solid idea of what rag is all about. To help you understand rag, we're going to walk through a very quick example. So I want you to imagine that you have a very large financial document, like the one seen on the right-hand side. There might be a tremendous amount of text in this. It might have anywhere from, who knows, a hundred to a thousand pages. And we might want to ask, Claude, very specific questions about very specific areas of the document. For example, we might want to ask a question like, what risk factors does this company have? Now, presumably, this document might have some relevant information inside of it. So we need to solve a very fundamental issue here. How do we get some information out of this document and into Claude so it can help us answer our question? I want to show you two possible ways that we could solve this problem. So option number one, we could take all of the text out of this document and just place it directly into a prompt, like the one you see on the right hand side. So we might ask Claude to answer a user's question, we'll then put in the user question, and then take all the text out of the document and put it into the prompt as well. Now, this is perhaps not the best solution. It might work, it also might not. Just so you know, there is a hard limit on how much text we can feed into Claude. So if this document is really, really long and we take all the text out of it and feed all the text into Claude, we might immediately end up getting an error, which means just right off the gate, this solution would not work if our document is really, really long. The second problem with this approach is that Claude gets a little bit less effective as your prompt gets longer. So if you start putting a tremendous amount of text into a prompt, Claude is going to have just harder time understanding exactly what you want and answering your question because there is just a tremendous amount of information inside the prompt. And then finally, larger prompts cost more money to process and take longer to process. So there's a financial burden here as well and a user experience burden because they just have to wait around longer to get back some kind of answer. So option number one might work in some scenarios, in other scenarios, it might fail entirely. So at that point, let's take a look at option number two. Option number two is a little bit more complex. So Option number two has two separate steps. In step one, we'll take all the text out of the document and break it up into small chunks. Then whenever a user asks a question, we're going to take their question and put it into the prompt as before. But we're also going to go through an extra little step. We're going to examine the user's question very closely. And we're going to find a chunk of text that seems most relevant to the user's question. In this case, if a user asks us what risk does this company face, and we have a chunk of text right here that seems to be about risk factors, we would then take that chunk of text and include it inside of the prompt. So now we are focusing all of Claude's attention on just this very small snippet of the overall financial document. And hopefully Claude can do a much better job of answering the user's question than before when we were just putting all of the text of the document into the prompt. So option number two has a distinct set of upsides and downsides. The upsides here are that Claude can focus on just the relevant content. Secondly, this can scale up to really, really large documents with a tremendous number of pages. And it also works if we have multiple documents. We can take all these different documents, separate them all into chunks, and then once again, only include chunks relevant to user's question inside of a prompt. This technique also generally leads to much smaller prompts, which means it's going to take less time to run and it's going to cost us a lot less. But there are some big downsides to this approach as well. First off, there's just naturally a lot more complexity. This requires a pre-processing step, where we take all the text out of the document and split it into chunks. We also have to figure out some way of searching through all these chunks to find the ones that are most relevant to the user's question, and we even need to define what it means to be relevant to the user's question. When we do find some relevant chunks and include them in the prompt, there's really no guarantee that they will contain all the context that Claude needs to actually answer the question. If the user asks what risk does this company face and include only the risk factor section, that might include some other important area of the document, maybe strategy outlook, where some of those risks get addressed in some way. And then finally, there are many different ways in which we can split the text up. So we could just take all the text of the document and divide it into equal portions. Or we could go through the document and find all these different headers and say for every header, we're going to make a new chunk. So we might have chunk one and then two and then three somewhere down here. There are many different ways in which we can define what a chunk is. And so we have to do a little bit of evaluation and decide which technique is the best for our particular application. So as you might guess, option number two is rag. It is retrieval augmented generation. As we just discussed, rag has many big upsides and many big downsides as well. There's a lot of technical challenges around it. It requires a pre-processing step. We also have to figure out some kind of searching mechanism to find those relevant chunks. We have to chunk documents. All in all, there's just a lot more work than option number one. So whenever we are considering implementing rag inside an application, we really have to analyze all these different steps and figure out whether or not it is right for our particular use case. All right, so now we have kind of a very, very high level understanding of what rag is all about. Let's start to take a look at the actual implementation of this process in just a moment.

---

## 🎬 トランスクリプト（日本語）

このモジュールでは、非常に大きな リトリーバル拡張生成、または略してragと呼ばれるテクニックについて 詳しく説明します。 このビデオでは特に、ragがどのようなものかについて、非常に明確な 考えをお伝えしたいと思います。ragを理解するために、 非常に簡単な例を見ていきましょう。 そのため、非常に大きな 財務書類、右側に見えるようなものがあると想像してください。これには 膨大な量のテキストが含まれているかもしれません。100から1000ページもの テキストが含まれているかもしれません。そして、Claudeに、 書類の非常に具体的な領域について、非常に具体的な質問を したいかもしれません。例えば、 この会社にはどのようなリスク要因がありますか？といった質問を するかもしれません。この書類には 関連する情報が含まれているはずです。そのため、 ここに非常に基本的な問題を解決する必要があります。この書類から 情報をClaudeに取り込んで、質問に答えられるようにするには どうすればよいでしょうか？この問題を解決するための 可能な方法を2つご紹介します。 オプション1として、この書類からすべてのテキストを取り出し、右側に見えるようなプロンプトに直接 配置することができます。Claudeにユーザーの質問に答えるように指示し、 次にユーザーの質問を入力し、その後書類からすべてのテキストを 取り出してプロンプトに配置します。 これはおそらく最善の解決策ではありません。 機能する場合もあれば、機能しない場合もあります。 Claudeに渡すことができるテキストの量には上限があります。そのため、この書類が非常に長い場合、すべてのテキストを取り出してClaudeに渡すとすぐにエラーが発生する可能性があり、 つまり、最初の段階でこの解決策は、書類が非常に長い場合には機能しない可能性があります。 このアプローチの2番目の問題は、プロンプトが長くなるにつれてClaudeの効果が少し低下することです。 そのため、膨大な量のテキストをプロンプトに入れると、Claudeは 具体的に何を求めているのかを理解し、質問に答えるのが難しくなります。 なぜなら、プロンプトの中に膨大な量の情報があるからです。そして最後に、 プロンプトが大きいほど、処理にかかるコストと時間がかかります。 そのため、ここに経済的な負担と、ユーザーエクスペリエンスの負担もあり、 回答を得るために長い間待たなければならないからです。 したがって、オプション1は一部のシナリオでは機能するかもしれませんが、他のシナリオでは完全に失敗する可能性があります。 そのため、ここでオプション2を見てみましょう。オプション2は少し複雑です。 オプション2には2つの別々のステップがあります。ステップ1では、 書類からすべてのテキストを取り出して小さなチャンクに分割します。 次に、ユーザーが質問をすると、以前と同様にプロンプトに 入力します。しかし、追加のステップを1つ実行します。ユーザーの質問を注意深く調べます。 そして、ユーザーの質問に最も関連性の高いと思われるテキストのチャンクを見つけます。 この場合、ユーザーがこの会社にはどのようなリスクがありますか？と質問し、 ここにリスク要因に関するテキストのチャンクがある場合、 そのテキストのチャンクを取得してプロンプトに含めます。 したがって、これでClaudeの注意を 財務書類全体の非常に小さなスニペットに集中させます。そして、うまくいけば、 書類全体のテキストをプロンプトに入れたときよりも、Claudeはユーザーの質問に より良く答えられるでしょう。 したがって、オプション2には明確な長所と短所があります。 ここでの長所は、Claudeが関連するコンテンツにのみ集中できることです。第二に、 これは本当に本当に長い書類にも対応できます。 そして、複数の書類がある場合にも機能します。 これらの異なる書類すべてを取り出し、すべてをチャンクに分割し、 そして再び、ユーザーの質問に関連するチャンクのみをプロンプトに含めます。 このテクニックは一般的にプロンプトがはるかに小さくなるため、実行時間が短縮され、 コストも大幅に削減されます。しかし、このアプローチには いくつかの大きな欠点もあります。まず、 当然ながら、はるかに多くの複雑さが伴います。 これには前処理ステップが必要であり、書類からすべてのテキストを取り出し、 チャンクに分割します。また、最も関連性の高いチャンクを見つけるために、 これらのチャンクすべてを検索する方法を考え出す必要もあります。 また、ユーザーの質問に関連するとはどういうことかを定義する必要すらあります。 関連するチャンクが見つかり、それらをプロンプトに含めた場合、 それらがClaudeが質問に答えるために必要なすべてのコンテキストを含んでいるとは限りません。 ユーザーがこの会社にはどのようなリスクがありますか？と質問し、リスク要因セクションのみを含めた場合、 戦略の見通しなど、リスクが何らかの形で対処されている他の重要な領域が含まれる可能性があります。 そして最後に、テキストを分割する方法はたくさんあります。 そのため、書類からすべてのテキストを取り出し、均等な部分に分割することができます。 あるいは、書類を調べて、これらのさまざまなヘッダーすべてを見つけ出し、 ヘッダーごとに新しいチャンクを作成すると言うこともできます。 したがって、チャンク1、2、そしてここにある3などがあります。 チャンクとは何かを定義する方法はたくさんあります。 そのため、評価を行い、どのテクニックが特定のアプリケーションに最適かを決定する必要があります。 したがって、推測されるように、オプション2は rag、つまりリトリーバル拡張生成です。 先ほど説明したように、ragには多くの大きな長所と、 多くの大きな欠点もあります。 それには多くの技術的な課題があります。前処理ステップが必要です。 関連するチャンクを見つけるための検索メカニズムも考え出す必要があります。 書類をチャンクに分割する必要があります。すべてを考慮すると、オプション1よりもはるかに多くの作業があります。 したがって、アプリケーションにragを実装することを検討する際には、 これらのさまざまなステップをすべて分析し、それが特定のユースケースに適しているかどうかを 判断する必要があります。 さて、ragがどのようなものかについて、非常に高レベルの理解を得られたと思います。 これから、このプロセスの実際の実装を調べていきましょう。 まもなく。
