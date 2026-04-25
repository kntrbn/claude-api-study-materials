# 19. Running the eval

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287743
**Section:** 04 Prompt evaluation

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Running the eval
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Now that we have our evaluation dataset ready, it's time to build the core evaluation pipeline. This involves taking each test case, merging it with our prompt, feeding it to Claude, and then grading the results.

The evaluation process follows a clear workflow: we take our dataset of test cases, combine each one with our prompt template, send it to Claude for processing, and then evaluate the output using a grader system.

Building the Core Functions

The evaluation pipeline consists of three main functions, each with a specific responsibility. Let's start with the simplest one - the function that handles individual prompts.

The run_prompt Function

This function takes a test case and merges it with our prompt template:

def run_prompt(test_case):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
Please solve the following task:

{test_case["task"]}
"""
    
    messages = []
    add_user_message(messages, prompt)
    output = chat(messages)
    return output

Right now, we're keeping the prompt extremely simple. We're not including any formatting instructions, so Claude will likely return more verbose output than we need. We'll refine this later as we iterate on our prompt design.

The run_test_case Function

This function orchestrates running a single test case and grading the result:

def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)
    
    # TODO - Grading
    score = 10
    
    return {
        "output": output,
        "test_case": test_case,
        "score": score
    }

For now, we're using a hardcoded score of 10. The grading logic is where we'll spend significant time in upcoming sections, but this placeholder lets us test the overall pipeline.

The run_eval Function

This function coordinates the entire evaluation process:

def run_eval(dataset):
    """Loads the dataset and calls run_test_case with each case"""
    results = []
    
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    
    return results

This function processes every test case in our dataset and collects all the results into a single list.

Running the Evaluation

To execute our evaluation pipeline, we load our dataset and run it through our functions:

with open("dataset.json", "r") as f:
    dataset = json.load(f)

results = run_eval(dataset)

The first time you run this, expect it to take some time - even with Claude Haiku, it can take around 30 seconds to process a full dataset. We'll cover optimization techniques later.

Examining the Results

The evaluation returns a structured JSON array where each object represents one test case result:

print(json.dumps(results, indent=2))

Each result contains three key pieces of information:

output: The complete response from Claude
test_case: The original test case that was processed
score: The evaluation score (currently hardcoded)

As you can see in the output, Claude generates quite verbose responses since we haven't provided specific formatting instructions yet. This is exactly the kind of issue we'll address as we refine our prompts.

What We've Accomplished

At this point, we've successfully built the core evaluation pipeline. We can take our dataset, process it through Claude, and collect structured results. The major missing piece is the grading system - that hardcoded score of 10 needs to be replaced with actual evaluation logic.

This pipeline represents the foundation of most AI evaluation systems. While it may seem simple, you've just built the majority of what an eval pipeline actually does. The complexity comes in the details - better prompts, sophisticated grading, and performance optimizations.

Next, we'll dive into the critical topic of graders, which will transform our hardcoded scores into meaningful evaluations of Claude's performance.

---

## 🎬 Transcript (English)

With our data set generation complete, we now need to take every record in that data set, which we're going to refer to as a test case. So we're going to take each test case and merge it with the prompt. We're then going to take the result and feed it into Claude. And then once we have all these different outputs, we're going to feed them through our grader. Remember, we have not discussed graders just yet. Don't worry, that's going to come up very quickly. And once again, just to save a little bit of time, I've written out a little bit of code here just to help guide this next phase of our workflow. I put together three separate functions with a very clear comment on what each one does. The first one that's easiest to understand is the run prompt function. This is going to be called with a test case. And those JSON objects we generated just a moment ago, each of these is a test case. So you can imagine that each of these one by one are going to flow into the run prompt function. So inside of here, our goal is to merge that task that we generated with our prompt, generate some text with Claude, and then return the result. So let's do that right away. I'm going to put in my V1 prompt right here, which is very simple. Remember, we are starting off as simple as possible here. So it'll just say something like, please solve the following task. And I want this to be a F string and I'm going to put in test case task. Next up, we want to send this off to Claude. So I'll make a list of messages. I'll add in a user message. I'm then going to pass this off to Claude by calling chat. And we're going to get back some resulting text, some result, or maybe we'll call it output this time around. And then for right now, I'll just return the output. Now remember, we don't have any kind of formatting included or any formatting instructions inside the prompt right now. So we're going to probably get back a lot more output than we ever asked for. The real goal of our prompt is to make sure that we get just Python or JSON or that regular expression. And we don't have anything for that right now. So we'll almost definitely have to come back and make some improvements. But for right now, we at least have a start to run prompt. The next thing we're going to work on is run test case. The goal of this function is to take in one of those individual cases, call the run prompt function we just put together, get some output from Claude, and then grade the result and return a dictionary describing the and everything that happened there. Now that sounds really complicated, but in reality, it's going to be surprisingly simple. So let me show you all we have to do here. We're going to put in output that's going to come from calling the function that we were just working on a moment ago. So this run prompt function. Put in our test case and then we're going to do some grading right here that's going to be a to do. Right now, I'll just say that we have a hard coded score of 10. So we definitely have to come back and do a lot of heavy lifting right there. And then at the bottom, we're just going to return some information that summarizes everything about running this test case. So I'll return a dictionary with some output. Give me whatever got back from Claude. I'll include the test case. And then our score. And then one final step here, we have to implement RunEval. So this function is going to load up our data set or receive it as an argument, either one is fine. And then we're going to loop through that data set. And for every test case, we will call run test case and then just assemble all the results together. So for our implementation here, I'll say results. It's going to start off as an empty list. And for every test case in data set, I'm going to get our result. from calling run test case and pass in the test case to it. And then add that into our list of results. And then down here, I'm just going to print up all of our results. Actually, let's actually just go ahead and return results. That's a little bit better. Okay, so there's the outline for our three major functions. Now believe it or not, this is like a vast majority of what a eval pipeline is. We just put together the vast majority with the obvious exception of grading. So as you can see, there's not a whole lot of code that goes into this. Let's now test this out. So down here in the next cell down, I'm going to go into open up our data set JSON file. And parse it as JSON. And then call the runEval function. That's the one that we were just putting together right here with the entire data set. Finally, I'm going to assign the result to that to results. I'm going to rerun all the cells above, just to make sure that I executed all of them, and then I'm going to run the cell. We'll see what happens. And just so you know, the first time you run this, it is going to take a pretty good amount of time, even if you are using high-coup. It's going to end up taking me about 31 seconds to complete this with high-coup. I'm going to show you some techniques for speeding up our eval run time, but for right now, we're just going to have it take a little bit longer, but don't worry, we will speed it up. So now let's take a look at results and see what we have. Results is going to be a rather large JSON object. So I'm going to print it out really nicely with a print, JSON dumps, with results, and an indent of two. There we go. So now we get an array of objects. Every object represents the output from one of our individual test cases. I've got the output right here. That's the output coming from Claude. And we can see there is a lot of stuff generated here. And if I scroll down a little bit, I'll see the definition of the test case that this was based upon. And then the score, which again right now is just hard coded at 10. And then that's just going to repeat over and over again. All right, so at this point in time, we have successfully gone through this step right here. We merged together our data set with our test prompt and we got some output from Claude and we kind of collated all this stuff together. So now the last thing we really have to do here is take the input and the result that we got out of Claude and feed it into one of these different graders. So this finally is the time where we're going to start to learn about graders. We're going to start to discuss them in the next video.

---

## 🎬 トランスクリプト（日本語）

データセット生成が完了したので、 そのデータセットの各レコードを、テストケースと呼びます。 テストケースをそれぞれプロンプトとマージします。 そして、その結果を取得し、Claudeに入力します。 これらの様々な出力がすべて揃ったら、 それらをグレーダーに入力します。 グレーダーについては、まだ説明していません。 心配しないでください、すぐに説明します。 そしてもう一度、少し時間を節約するために、 この次の段階をガイドするコードを少し書いておきました。 3つの独立した関数を作成しました。 それぞれの機能について、非常に明確なコメントを付けました。 一番理解しやすいのはrun_prompt関数です。 これはテストケースとともに呼び出されます。 そして、先ほど生成したJSONオブジェクト これらの各々はテストケースです。 つまり、これらの各ものが一つずつ、 run_prompt関数に流れていくと想像できます。 つまり、 この中での目標は、生成したタスクを プロンプトとマージすることです。 Claudeでテキストを生成し、結果を返します。 では、すぐにそれを実行しましょう。 ここにV1プロンプトを 入力します。 これは非常にシンプルです。 ここでは可能な限りシンプルに始めています。 だから、例えば「以下のタスクを解決してください。」 のように言います。 そして、これをF文字列にします。 そして、test_case['task']を入れます。 次に、Claudeに送信します。 メッセージのリストを作成します。 ユーザーメッセージを追加します。 そして、これをClaudeに渡します。 チャットを呼び出して。 そして、結果のテキスト、 結果、または今回は出力と呼びましょう、 それを受け取ります。 そして、今のところは出力を返すだけです。 覚えておいてください、 現時点では、プロンプトにフォーマットは含まれていません。 またはフォーマットの指示もありません。 だから、おそらく要求した以上の出力が 返ってくるでしょう。 プロンプトの本当の目的は、 Python、JSON、 または正規表現だけを取得することです。 そして、現時点ではそのためのものは何もありません。 だから、ほぼ間違いなく戻ってきて 改善を行う必要があります。 しかし、今のところは、 run_promptの開始点があります。 次に、run_test_caseに取り組みます。 この関数の目標は、個々のケースの1つを受け取り、 先ほど作成したrun_prompt関数を呼び出し、 Claudeから出力を取得し、 結果を評価して、 そこでのすべての出来事を記述した辞書を返すことです。 それは非常に複雑に聞こえるかもしれませんが、 実際には驚くほどシンプルになります。 だから、ここで行うすべてを示します。 先ほど作業していた関数を呼び出した結果の 出力が入ります。 つまり、このrun_prompt関数です。 テストケースを入れ、そしてここで評価を行います。 これは後でやること（todo）になります。 今のところ、スコアは10のハードコーディングです。 だから、間違いなく戻ってきて そこで多くの作業を行う必要があります。 そして、一番下に、テストケースの実行に関する すべての情報を要約するものを返します。 だから、辞書を返します。 Claudeから返された 出力をください。 テストケースを含めます。 そして、スコアも。 そして、最後の1ステップ。 RunEvalを実装する必要があります。 この関数は、データセットをロードするか、 引数として受け取ります。どちらでも構いません。 そして、データセットをループします。 そして、すべてのテストケースに対して、 run_test_caseを呼び出し、 すべての結果をまとめます。 なので、 ここでの実装では、結果とします。 空のリストから開始します。 データセット内の各テストケースについて、 結果を取得します。 run_test_caseを呼び出して テストケースを渡します。 そして、それを結果のリストに追加します。 そして、ここでは、すべての 結果を印刷します。 実際には、返しましょう。 結果を返しましょう。それはもう少し良いです。 OK、 これで3つの主要な関数の概要ができました。 信じられないかもしれませんが、これは 評価パイプラインの大部分です。 私たちが今作り上げたのは大部分です。 もちろん、評価の部分を除いて。 ご覧のとおり、これにはそれほど多くのコードは必要ありません。 これをテストしてみましょう。 下の次のセルで、 データセットのJSONファイルを開きます。 そしてJSONとして解析します。 そして、runEval関数を呼び出します。 これは、先ほど作成した 関数です。 データセット全体と一緒に。 最後に、結果を resultsに代入します。 すべてのセルを再実行して、 すべて実行したことを確認します。 そして、セルを実行します。 何が起こるか見てみましょう。 そして、知っておいてほしいのですが、 初めて実行するときは、 多くの時間が必要になります。 ハイクープを使用している場合でも、 完了するのに約31秒かかります。 ハイクープで。 評価実行時間を短縮するためのテクニックを紹介しますが、 今のところは、少し長くかかりますが、 心配しないでください、短縮します。 では、結果を見てみましょう。 結果はかなり大きなJSONオブジェクトになります。 だから、JSONダンプでインデントを2にしてきれいに印刷します。 これで完了です。 これで、オブジェクトの配列が表示されます。 各オブジェクトは、 個々のテストケースの1つからの出力を表します。 ここにその出力があります。 これはClaudeからの出力です。 そして、ここに多くのものが生成されているのがわかります。 そして、少しスクロールすると、 これが基づいていたテストケースの定義と、 スコアが表示されます。 これも今は10とハードコーディングされています。 そして、それが繰り返し続きます。 よし、この時点で、 このステップを正常に完了しました。 データセットとテストプロンプトを組み合わせ、 Claudeから出力を取得し、 これらのものをすべてまとめました。 なので、最後に本当にする必要があるのは、 入力とClaudeから取得した結果を これらの異なるグレーダーの1つに入力することです。 なので、ついにグレーダーについて学ぶ時です。 次のビデオで議論を開始します。
