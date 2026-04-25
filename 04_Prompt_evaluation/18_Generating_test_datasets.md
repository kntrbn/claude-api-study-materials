# 18. Generating test datasets

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287739
**Section:** 04 Prompt evaluation

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Generating test datasets
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Building a custom prompt evaluation workflow starts with creating a solid prompt and then generating test data to see how well it performs. Let's walk through setting up an evaluation system for a prompt that helps users write AWS-specific code.

Setting Up the Goal

Our prompt needs to assist users in writing three specific types of output for AWS use cases:

Python code
JSON configuration files
Regular expressions

The key requirement is that when a user requests help with a task, we return clean output in one of these formats without any extra explanations, headers, or footers.

Here's our starting prompt (version 1):

prompt = f"""
Please provide a solution to the following task:
{task}
"""

Creating an Evaluation Dataset

An evaluation dataset contains inputs that we'll feed into our prompt. For each combination of prompt and input, we'll run the prompt and analyze the results.

Our dataset will be an array of JSON objects, where each object contains a "task" property describing what we want Claude to accomplish. We can either create this dataset by hand or generate it automatically using Claude.

Since we're generating test data, this is a perfect opportunity to use a faster model like Haiku instead of the full Claude model.

Generating Test Data with Code

Let's create a function that automatically generates our test dataset. First, we'll need our helper functions for working with Claude:

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    if system:
        params["system"] = system
    if stop_sequences:
        params["stop_sequences"] = stop_sequences
    
    response = client.messages.create(**params)
    return response.content[0].text

Now we'll create our dataset generation function:

def generate_dataset():
    prompt = """
Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of JSON objects, each representing task that requires Python, JSON, or a Regex to complete.

Example output:
```json
[
  {
    "task": "Description of task",
  },
  ...additional
]
```

* Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
* Focus on tasks that do not require writing much code

Please generate 3 objects.
"""

To properly parse the JSON response, we'll use prefilling and stop sequences:

    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)

Testing the Dataset Generation

Let's run our function and see what kind of test cases we get:

dataset = generate_dataset()
print(dataset)

This should return three different test cases covering our target outputs - Python functions, JSON configurations, and regular expressions for AWS-specific tasks.

Saving the Dataset

Once we have our dataset, we'll save it to a file so we can easily load it later during evaluation:

with open('dataset.json', 'w') as f:
    json.dump(dataset, f, indent=2)

This creates a dataset.json file in the same directory as your notebook, containing your list of tasks ready for prompt evaluation.

With this foundation in place, you now have a systematic way to generate test data for evaluating how well your prompts perform

---

## 🎬 Transcript (English)

Let's get started on building our own custom prompt evaluation workflow. We're going to be writing out a prompt and then writing out some code to evaluate how well it performs. So let's first focus on making a prompt. The goal of our prompt is to help users in writing out some code specific for AWS use cases. So we're going to allow user to enter in some kind of task that they need help with. And then we're going to respond with one of three types of output. We're either going to output Python, JSON configuration, or a raw, just plain regular expression. Those are our three possible outputs. So we need to make sure that whenever a user asks for us to complete some kind of task, we give them some output in one of these three particular outputs without any other kind of explanation, or header, or footer, or anything like that. So that's the overall goal. Now, the first step of our goal is, of course, to write out a draft prompt. Now, I've kind of already done that for us on the right-hand side here. I've got V1 of our prompt, where it just says, please provide a solution to the following task, and we'll put the user's task in there. Step two is to assemble a data set. Remember that a data set is going to contain some number of inputs that we're going to feed into our prompt, and then we're going to run our prompt for every combination of prompt and input. For our particular case, we're going to have an array of JSON objects, where every object has a task property. These tasks are going to describe something that we want to be done by Claude, so we're going to take each of these tasks, put them into our prompt, and then feed the result into Claude. Remember that when we make a data set, we can either assemble it by hand, or we can generate it automatically with Claude. Now, as a side note, if you're using Claude for something like this, this would be a really good opportunity to use a faster model like Haiku. And that's what we're going to be doing here. Let's go back on to Jupyter, we're going to open up our notebook, and we're going to write out a little bit of code that's going to generate a sample data set, like the one you see on the left-hand side, using Haiku. Back over here, I've created a new notebook, it has a lot of the same code that we've been working on throughout the course. So I'm creating a client inside the top cell and also loading some environment variables, and I create those same three helper functions that we've been developing. Then, a little bit lower, I've defined a function called generate data set. And inside of here, I've put together a rather large prompt to get us started. Now, I've taken this notebook and attached it to this lecture. So I would encourage you to download this notebook and copy the prompt right here, or just use this notebook directly to save yourself a whole bunch of typing. This prompt is going to ask Claude to go ahead and generate some different test cases for us. Our test cases are going to be represented by an array of JSON objects, and each object is going to have a task property that describes the task to be done. For right now, I'm just asking Claude to generate three such objects. This is enough to definitely get us started and make sure that we can actually create a data set. So now let's add in some code to this generate dataset function that we are in. It will actually take this prompt, send off to Claude, get back a list of tasks, and then parse them as JSON. To parse the JSON, we're going to make sure that we use that same prefilling and stop sequence method. We spoke about a little bit ago. So let's get to it. Down here inside of the function, so I'm going to make sure that I do indent in, I will declare a list of messages. I'll add a user message, of that prompt, I'll then add in an assistant message, and I'm going to put in backtick, backtick, backtick, JSON. I'll then call it chat with our listed messages and some stop sequences. In this case, our only stop sequence is going to be backtick, backtick, backtick. And then finally, I will return JSON.loads, text. OK, so I'm going to run the cell to make sure that function gets defined, and we'll test it out down here really quickly. And then let's print up that data set just to make sure that we are getting back some realistic looking data. Okay, there we go. So there's our three different test cases. We are getting a case in which we are going to get a Python function, write some JSON configuration, and then write a regular expression. So let's say this is a good start. Next, I would like to take this data set and write it into a file. So we can very easily load it up later on when we start to evaluate our prompt to do so. We will open up a file in my right mode. I'm going to call the file dataset.json. and then json.dump with an indent of two. So I'm going to run this again. After that cell runs inside the same directory as my notebook, I should find a dataset.json file and inside there should be our list of tasks. Okay, this is a good start. We've got our eval dataset put together.

---

## 🎬 トランスクリプト（日本語）

独自のカスタムプロンプト評価ワークフローの構築を始めましょう。 プロンプトを作成し、そのパフォーマンスがどれだけ優れているかを評価するためのコードを作成します。 まずはプロンプト作成に集中しましょう。私たちのプロンプトの目標は、 ユーザーがAWSのユースケースに特化したコードを書くのを助けることです。 ユーザーが助けを必要としているタスクを入力できるようにし、 そのタスクに対して3種類の出力のいずれかで応答します。 Python、JSON設定、 または生の、単純な正規表現のいずれかを出力します。 それらが私たちの3つの可能な出力です。 ユーザーがタスクの完了を依頼するときは、 これらの3つの出力のいずれかで、 説明、ヘッダー、フッターなどを一切含まずに出力する必要があります。 それが全体的な目標です。 私たちの目標の最初のステップは、もちろんドラフトプロンプトを作成することです。 右側に、すでにバージョン1のプロンプトを作成しました。 「次のタスクの解決策を提供してください」とだけ書かれており、 そこにユーザーのタスクを挿入します。ステップ2はデータセットの組み立てです。 データセットには、プロンプトに供給する入力がいくつか含まれることを忘れないでください。 そして、プロンプトと入力のすべての組み合わせに対してプロンプトを実行します。 今回のケースでは、各オブジェクトがタスクプロパティを持つJSONオブジェクトの配列を用意します。 これらのタスクは、Claudeに実行してほしいことを説明するものです。 したがって、これらのタスクのそれぞれを取得し、プロンプトに挿入し、 その結果をClaudeに渡します。 データセットを作成するとき、手動で組み立てるか、 Claudeを使って自動生成できることを思い出してください。 サイドノートとして、このような目的でClaudeを使用する場合、 Haikuのような高速なモデルを使用するのは非常に良い機会でしょう。 ここではそれを行います。Jupyterに戻り、ノートブックを開き、 左側に見えるようなサンプルデータセットを生成する簡単なコードを作成します。 ここに移動しました。新しいノートブックを作成しました。 コース全体で作業してきたコードの多くが含まれています。 そのため、一番上のセルでクライアントを作成し、環境変数も読み込んでいます。 そして、これまで開発してきたのと同じ3つのヘルパー関数を作成します。 そして、もう少し下に、generate_datasetという名前の関数を定義しました。 そして、その中で、かなり大きなプロンプトを準備しました。 このノートブックをこの講義に添付しました。 このノートブックをダウンロードして、ここにあるプロンプトをコピーするか、 このノートブックを直接使用して、タイピングの手間を省くことをお勧めします。 このプロンプトは、Claudeにいくつかの異なる テストケースを生成するように依頼するものです。 テストケースはJSONオブジェクトの配列として表され、 各オブジェクトには、実行されるタスクを説明するタスクプロパティがあります。 現時点では、Claudeにそのようなオブジェクトを3つ生成するように依頼しています。 これは、データセットを作成できることを確実に確認するための十分な量です。 それでは、このgenerate_dataset関数にコードを追加しましょう。 この関数は、このプロンプトをClaudeに送信し、 タスクのリストを取得し、それをJSONとして解析します。 JSONを解析するために、先ほど少し話した 同じ事前充填と停止シーケンスの方法を使用します。 それでは始めましょう。 関数の下に行きましょう。インデントするようにします。 メッセージのリストを宣言します。 ユーザーメッセージとしてそのプロンプトを追加し、 アシスタントメッセージを追加します。 そして、バッククォート、バッククォート、バッククォート、JSONを入れます。 次に、メッセージのリストと停止シーケンスでチャットを呼び出します。 この場合、唯一の停止シーケンスはバッククォート、バッククォート、バッククォートになります。 そして最後に、json.loads(text)を返します。 OK、その関数が定義されていることを確認するためにセルを実行します。 ここで非常に素早くテストします。 そして、データセットを印刷して、 現実的なデータが取得できていることを確認しましょう。 はい、できました。これが3つの異なるテストケースです。 Python関数を取得するケース、JSON設定を作成するケース、 そして正規表現を作成するケースがあります。 これは良いスタートと言えるでしょう。次は、 このデータセットを取得してファイルに書き込みたいと思います。 これにより、プロンプトの評価を開始するときに簡単にロードできます。 そのためには、書き込みモードでファイルを開きます。 ファイル名をdataset.jsonとし、 インデントを2にしてjson.dumpを使用します。 これを再度実行します。 セルの実行後、ノートブックと同じディレクトリ内に dataset.jsonファイルが見つかるはずです。 そしてその中にタスクのリストがあります。 よし、これは良いスタートです。評価データセットを用意できました。
