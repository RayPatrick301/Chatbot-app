import tensorflow as tf
from collections import namedtuple

# Model Parameters
tf.flags.DEFINE_integer("vocab_size", 91620, "")
tf.flags.DEFINE_integer("embedding_dim", 50, "")
tf.flags.DEFINE_integer("rnn_dim", 256, "")
tf.flags.DEFINE_integer("max_context_len", 80, "")
tf.flags.DEFINE_integer("max_utterance_len", 40, "")
tf.flags.DEFINE_float("dropout_keep_prob", 1.0, "")

# Pre-trained embeddings
tf.flags.DEFINE_string("glove_path", None, "Path to pre-trained Glove vectors")
tf.flags.DEFINE_string("vocab_path", None, "Path to vocabulary.txt file")

# Training Parameters
tf.flags.DEFINE_float("learning_rate", 0.001, "")
tf.flags.DEFINE_integer("batch_size", 64, "")
tf.flags.DEFINE_integer("eval_batch_size", 8, "")
tf.flags.DEFINE_string("optimizer", "Adagrad", "")

FLAGS = tf.flags.FLAGS

HParams = namedtuple(
  "HParams",
  [
    "batch_size",
    "dropout_keep_prob",
    "embedding_dim",
    "eval_batch_size",
    "learning_rate",
    "max_context_len",
    "max_utterance_len",
    "optimizer",
    "rnn_dim",
    "vocab_size",
    "glove_path",
    "vocab_path"
  ])

def create_hparams():
  return HParams(
    batch_size=FLAGS.batch_size,
    eval_batch_size=FLAGS.eval_batch_size,
    vocab_size=FLAGS.vocab_size,
    dropout_keep_prob=FLAGS.dropout_keep_prob,
    optimizer=FLAGS.optimizer,
    learning_rate=FLAGS.learning_rate,
    embedding_dim=FLAGS.embedding_dim,
    max_context_len=FLAGS.max_context_len,
    max_utterance_len=FLAGS.max_utterance_len,
    glove_path=FLAGS.glove_path,
    vocab_path=FLAGS.vocab_path,
    rnn_dim=FLAGS.rnn_dim)