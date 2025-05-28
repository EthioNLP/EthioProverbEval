# ProverbEval: LLM Evaluation for Low-Resource Language Understanding

This repository contains the YAML configuration files for the **ProverbEval** benchmark, designed for evaluating Large Language Models (LLMs) on their understanding of proverbs in low-resource Ethiopian languages (Amharic, Afaan Oromo, Tigrinya, Ge'ez) and English. The evaluations are intended to be run using the [EleutherAI Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).

The benchmark and its findings are detailed in the paper: "ProverbEval: Exploring LLM Evaluation Challenges for Low-resource Language Understanding."

## Tasks Overview

The YAML files in this repository define three main evaluation tasks:
1.  **Meaning Multiple Choice**: Models select the correct meaning of a proverb from four options.
2.  **Fill in the Blank**: Models complete a proverb by selecting the correct missing word.
3.  **Proverb Generation**: Models generate a proverb based on a given description.

These tasks are further broken down by language, prompt language (native or English), and other experimental conditions as described in the paper.

## How to Use

To use the evaluation tasks in this repository:

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/EthioNLP/EthioProverbEval.git
    cd EthioProverbEval
    ```

2.  **Ensure you have EleutherAI's `lm-evaluation-harness` installed and configured.** If not, please follow their [installation guide](https://github.com/EleutherAI/lm-evaluation-harness#installation).

3.  **Run evaluations using `lm-evaluation-harness`.**
    You will point the harness to the YAML configuration files located within the `choice/`, `fill_blank/`, and `generation/` directories of this repository.

    For example, to run the Amharic multiple-choice task with an English prompt and native language choices:
    ```bash
    # Make sure lm-eval is in your PATH or call it via python
    # The exact task name will correspond to the 'task' field in the YAML file.
    # You might need to register these tasks with the harness or specify the path to the YAML.

    # Example assuming tasks are registered or lm-eval can find them by path:
    lm_eval --model <your_model_name_or_path> \
            --tasks ethio_proverb_eval_amh_choice_prompt_english_native_choices # Adjust task name based on YAML
            # Or provide the direct path to the YAML file if that's how your harness is set up
            # --tasks path/to/your/specific_task.yaml 
            --device <cuda:0_or_cpu> \
            --batch_size auto \
            --output_path ./results/
    ```
    The specific task names (e.g., `ethio_proverb_eval_amh_choice_prompt_english_native_choices`) are defined within the YAML files themselves (usually under a `group` or `task` key). You'll need to refer to the YAML files for the exact task identifiers to pass to `lm-eval`.

    The YAML files are structured as follows:
    *   `choice/`: Contains configurations for the multiple-choice tasks.
        *   `prompts/`: Different prompt variations (e.g., English prompt, native prompt).
        *   `shuffle/`: Configurations for choice order sensitivity experiments.
        *   `translate-test/`: Configurations for proverb translation experiments.
    *   `fill_blank/`: Contains configurations for the fill-in-the-blank tasks.
    *   `generation/`: Contains configurations for the proverb generation tasks.

    Each subdirectory often contains further nesting by language and specific experimental setup (e.g., `choice/prompts/prompt-english/english/amh.yaml`).

## Citation

If you use ProverbEval or the data/configurations in this repository for your research, please cite:

```bibtex
@inproceedings{azime-etal-2025-proverbeval,
    title = "{P}roverb{E}val: Exploring {LLM} Evaluation Challenges for Low-resource Language Understanding",
    author = "Azime, Israel Abebe  and
      Tonja, Atnafu Lambebo  and
      Belay, Tadesse Destaw  and
      Chanie, Yonas  and
      Balcha, Bontu Fufa  and
      Abadi, Negasi Haile  and
      Ademtew, Henok Biadglign  and
      Nerea, Mulubrhan Abebe  and
      Yadeta, Debela Desalegn  and
      Geremew, Derartu Dagne  and
      Tesfu, Assefa Atsbiha  and
      Slusallek, Philipp  and
      Solorio, Thamar  and
      Klakow, Dietrich",
    editor = "Chiruzzo, Luis  and
      Ritter, Alan  and
      Wang, Lu",
    booktitle = "Findings of the Association for Computational Linguistics: NAACL 2025",
    month = apr,
    year = "2025",
    address = "Albuquerque, New Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-naacl.350/",
    pages = "6250--6266",
    ISBN = "979-8-89176-195-7"
}
```

For more details on the methodology, data collection, and experimental results, please refer to the [full paper](paper/2411.05049v3.pdf).
