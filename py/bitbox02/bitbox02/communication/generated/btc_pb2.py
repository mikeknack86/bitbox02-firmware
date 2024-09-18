# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: btc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2
from . import antiklepto_pb2 as antiklepto__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tbtc.proto\x12\x14shiftcrypto.bitbox02\x1a\x0c\x63ommon.proto\x1a\x10\x61ntiklepto.proto\"\xc6\x04\n\x0f\x42TCScriptConfig\x12G\n\x0bsimple_type\x18\x01 \x01(\x0e\x32\x30.shiftcrypto.bitbox02.BTCScriptConfig.SimpleTypeH\x00\x12\x42\n\x08multisig\x18\x02 \x01(\x0b\x32..shiftcrypto.bitbox02.BTCScriptConfig.MultisigH\x00\x12>\n\x06policy\x18\x03 \x01(\x0b\x32,.shiftcrypto.bitbox02.BTCScriptConfig.PolicyH\x00\x1a\xd9\x01\n\x08Multisig\x12\x11\n\tthreshold\x18\x01 \x01(\r\x12)\n\x05xpubs\x18\x02 \x03(\x0b\x32\x1a.shiftcrypto.bitbox02.XPub\x12\x16\n\x0eour_xpub_index\x18\x03 \x01(\r\x12N\n\x0bscript_type\x18\x04 \x01(\x0e\x32\x39.shiftcrypto.bitbox02.BTCScriptConfig.Multisig.ScriptType\"\'\n\nScriptType\x12\t\n\x05P2WSH\x10\x00\x12\x0e\n\nP2WSH_P2SH\x10\x01\x1aK\n\x06Policy\x12\x0e\n\x06policy\x18\x01 \x01(\t\x12\x31\n\x04keys\x18\x02 \x03(\x0b\x32#.shiftcrypto.bitbox02.KeyOriginInfo\"3\n\nSimpleType\x12\x0f\n\x0bP2WPKH_P2SH\x10\x00\x12\n\n\x06P2WPKH\x10\x01\x12\x08\n\x04P2TR\x10\x02\x42\x08\n\x06\x63onfig\"\xfc\x02\n\rBTCPubRequest\x12+\n\x04\x63oin\x18\x01 \x01(\x0e\x32\x1d.shiftcrypto.bitbox02.BTCCoin\x12\x0f\n\x07keypath\x18\x02 \x03(\r\x12\x41\n\txpub_type\x18\x03 \x01(\x0e\x32,.shiftcrypto.bitbox02.BTCPubRequest.XPubTypeH\x00\x12>\n\rscript_config\x18\x04 \x01(\x0b\x32%.shiftcrypto.bitbox02.BTCScriptConfigH\x00\x12\x0f\n\x07\x64isplay\x18\x05 \x01(\x08\"\x8e\x01\n\x08XPubType\x12\x08\n\x04TPUB\x10\x00\x12\x08\n\x04XPUB\x10\x01\x12\x08\n\x04YPUB\x10\x02\x12\x08\n\x04ZPUB\x10\x03\x12\x08\n\x04VPUB\x10\x04\x12\x08\n\x04UPUB\x10\x05\x12\x10\n\x0c\x43\x41PITAL_VPUB\x10\x06\x12\x10\n\x0c\x43\x41PITAL_ZPUB\x10\x07\x12\x10\n\x0c\x43\x41PITAL_UPUB\x10\x08\x12\x10\n\x0c\x43\x41PITAL_YPUB\x10\tB\x08\n\x06output\"k\n\x1a\x42TCScriptConfigWithKeypath\x12<\n\rscript_config\x18\x02 \x01(\x0b\x32%.shiftcrypto.bitbox02.BTCScriptConfig\x12\x0f\n\x07keypath\x18\x03 \x03(\r\"\xee\x02\n\x12\x42TCSignInitRequest\x12+\n\x04\x63oin\x18\x01 \x01(\x0e\x32\x1d.shiftcrypto.bitbox02.BTCCoin\x12H\n\x0escript_configs\x18\x02 \x03(\x0b\x32\x30.shiftcrypto.bitbox02.BTCScriptConfigWithKeypath\x12\x0f\n\x07version\x18\x04 \x01(\r\x12\x12\n\nnum_inputs\x18\x05 \x01(\r\x12\x13\n\x0bnum_outputs\x18\x06 \x01(\r\x12\x10\n\x08locktime\x18\x07 \x01(\r\x12H\n\x0b\x66ormat_unit\x18\x08 \x01(\x0e\x32\x33.shiftcrypto.bitbox02.BTCSignInitRequest.FormatUnit\x12\'\n\x1f\x63ontains_silent_payment_outputs\x18\t \x01(\x08\"\"\n\nFormatUnit\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x07\n\x03SAT\x10\x01\"\xc4\x03\n\x13\x42TCSignNextResponse\x12<\n\x04type\x18\x01 \x01(\x0e\x32..shiftcrypto.bitbox02.BTCSignNextResponse.Type\x12\r\n\x05index\x18\x02 \x01(\r\x12\x15\n\rhas_signature\x18\x03 \x01(\x08\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12\x12\n\nprev_index\x18\x05 \x01(\r\x12W\n\x1d\x61nti_klepto_signer_commitment\x18\x06 \x01(\x0b\x32\x30.shiftcrypto.bitbox02.AntiKleptoSignerCommitment\x12!\n\x19generated_output_pkscript\x18\x07 \x01(\x0c\x12!\n\x19silent_payment_dleq_proof\x18\x08 \x01(\x0c\"\x82\x01\n\x04Type\x12\t\n\x05INPUT\x10\x00\x12\n\n\x06OUTPUT\x10\x01\x12\x08\n\x04\x44ONE\x10\x02\x12\x0f\n\x0bPREVTX_INIT\x10\x03\x12\x10\n\x0cPREVTX_INPUT\x10\x04\x12\x11\n\rPREVTX_OUTPUT\x10\x05\x12\x0e\n\nHOST_NONCE\x10\x06\x12\x13\n\x0fPAYMENT_REQUEST\x10\x07\"\xea\x01\n\x13\x42TCSignInputRequest\x12\x13\n\x0bprevOutHash\x18\x01 \x01(\x0c\x12\x14\n\x0cprevOutIndex\x18\x02 \x01(\r\x12\x14\n\x0cprevOutValue\x18\x03 \x01(\x04\x12\x10\n\x08sequence\x18\x04 \x01(\r\x12\x0f\n\x07keypath\x18\x06 \x03(\r\x12\x1b\n\x13script_config_index\x18\x07 \x01(\r\x12R\n\x15host_nonce_commitment\x18\x08 \x01(\x0b\x32\x33.shiftcrypto.bitbox02.AntiKleptoHostNonceCommitment\"\xd7\x02\n\x14\x42TCSignOutputRequest\x12\x0c\n\x04ours\x18\x01 \x01(\x08\x12\x31\n\x04type\x18\x02 \x01(\x0e\x32#.shiftcrypto.bitbox02.BTCOutputType\x12\r\n\x05value\x18\x03 \x01(\x04\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x12\x0f\n\x07keypath\x18\x05 \x03(\r\x12\x1b\n\x13script_config_index\x18\x06 \x01(\r\x12\"\n\x15payment_request_index\x18\x07 \x01(\rH\x00\x88\x01\x01\x12P\n\x0esilent_payment\x18\x08 \x01(\x0b\x32\x38.shiftcrypto.bitbox02.BTCSignOutputRequest.SilentPayment\x1a \n\rSilentPayment\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\n\x16_payment_request_index\"\x99\x01\n\x1b\x42TCScriptConfigRegistration\x12+\n\x04\x63oin\x18\x01 \x01(\x0e\x32\x1d.shiftcrypto.bitbox02.BTCCoin\x12<\n\rscript_config\x18\x02 \x01(\x0b\x32%.shiftcrypto.bitbox02.BTCScriptConfig\x12\x0f\n\x07keypath\x18\x03 \x03(\r\"\x0c\n\nBTCSuccess\"m\n\"BTCIsScriptConfigRegisteredRequest\x12G\n\x0cregistration\x18\x01 \x01(\x0b\x32\x31.shiftcrypto.bitbox02.BTCScriptConfigRegistration\"<\n#BTCIsScriptConfigRegisteredResponse\x12\x15\n\ris_registered\x18\x01 \x01(\x08\"\xfc\x01\n\x1e\x42TCRegisterScriptConfigRequest\x12G\n\x0cregistration\x18\x01 \x01(\x0b\x32\x31.shiftcrypto.bitbox02.BTCScriptConfigRegistration\x12\x0c\n\x04name\x18\x02 \x01(\t\x12P\n\txpub_type\x18\x03 \x01(\x0e\x32=.shiftcrypto.bitbox02.BTCRegisterScriptConfigRequest.XPubType\"1\n\x08XPubType\x12\x11\n\rAUTO_ELECTRUM\x10\x00\x12\x12\n\x0e\x41UTO_XPUB_TPUB\x10\x01\"b\n\x14\x42TCPrevTxInitRequest\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x12\n\nnum_inputs\x18\x02 \x01(\r\x12\x13\n\x0bnum_outputs\x18\x03 \x01(\r\x12\x10\n\x08locktime\x18\x04 \x01(\r\"r\n\x15\x42TCPrevTxInputRequest\x12\x15\n\rprev_out_hash\x18\x01 \x01(\x0c\x12\x16\n\x0eprev_out_index\x18\x02 \x01(\r\x12\x18\n\x10signature_script\x18\x03 \x01(\x0c\x12\x10\n\x08sequence\x18\x04 \x01(\r\">\n\x16\x42TCPrevTxOutputRequest\x12\r\n\x05value\x18\x01 \x01(\x04\x12\x15\n\rpubkey_script\x18\x02 \x01(\x0c\"\xab\x02\n\x18\x42TCPaymentRequestRequest\x12\x16\n\x0erecipient_name\x18\x01 \x01(\t\x12\x42\n\x05memos\x18\x02 \x03(\x0b\x32\x33.shiftcrypto.bitbox02.BTCPaymentRequestRequest.Memo\x12\r\n\x05nonce\x18\x03 \x01(\x0c\x12\x14\n\x0ctotal_amount\x18\x04 \x01(\x04\x12\x11\n\tsignature\x18\x05 \x01(\x0c\x1a{\n\x04Memo\x12Q\n\ttext_memo\x18\x01 \x01(\x0b\x32<.shiftcrypto.bitbox02.BTCPaymentRequestRequest.Memo.TextMemoH\x00\x1a\x18\n\x08TextMemo\x12\x0c\n\x04note\x18\x01 \x01(\tB\x06\n\x04memo\"\xee\x01\n\x15\x42TCSignMessageRequest\x12+\n\x04\x63oin\x18\x01 \x01(\x0e\x32\x1d.shiftcrypto.bitbox02.BTCCoin\x12G\n\rscript_config\x18\x02 \x01(\x0b\x32\x30.shiftcrypto.bitbox02.BTCScriptConfigWithKeypath\x12\x0b\n\x03msg\x18\x03 \x01(\x0c\x12R\n\x15host_nonce_commitment\x18\x04 \x01(\x0b\x32\x33.shiftcrypto.bitbox02.AntiKleptoHostNonceCommitment\"+\n\x16\x42TCSignMessageResponse\x12\x11\n\tsignature\x18\x01 \x01(\x0c\"\x81\x05\n\nBTCRequest\x12_\n\x1bis_script_config_registered\x18\x01 \x01(\x0b\x32\x38.shiftcrypto.bitbox02.BTCIsScriptConfigRegisteredRequestH\x00\x12V\n\x16register_script_config\x18\x02 \x01(\x0b\x32\x34.shiftcrypto.bitbox02.BTCRegisterScriptConfigRequestH\x00\x12\x41\n\x0bprevtx_init\x18\x03 \x01(\x0b\x32*.shiftcrypto.bitbox02.BTCPrevTxInitRequestH\x00\x12\x43\n\x0cprevtx_input\x18\x04 \x01(\x0b\x32+.shiftcrypto.bitbox02.BTCPrevTxInputRequestH\x00\x12\x45\n\rprevtx_output\x18\x05 \x01(\x0b\x32,.shiftcrypto.bitbox02.BTCPrevTxOutputRequestH\x00\x12\x43\n\x0csign_message\x18\x06 \x01(\x0b\x32+.shiftcrypto.bitbox02.BTCSignMessageRequestH\x00\x12P\n\x14\x61ntiklepto_signature\x18\x07 \x01(\x0b\x32\x30.shiftcrypto.bitbox02.AntiKleptoSignatureRequestH\x00\x12I\n\x0fpayment_request\x18\x08 \x01(\x0b\x32..shiftcrypto.bitbox02.BTCPaymentRequestRequestH\x00\x42\t\n\x07request\"\x90\x03\n\x0b\x42TCResponse\x12\x33\n\x07success\x18\x01 \x01(\x0b\x32 .shiftcrypto.bitbox02.BTCSuccessH\x00\x12`\n\x1bis_script_config_registered\x18\x02 \x01(\x0b\x32\x39.shiftcrypto.bitbox02.BTCIsScriptConfigRegisteredResponseH\x00\x12>\n\tsign_next\x18\x03 \x01(\x0b\x32).shiftcrypto.bitbox02.BTCSignNextResponseH\x00\x12\x44\n\x0csign_message\x18\x04 \x01(\x0b\x32,.shiftcrypto.bitbox02.BTCSignMessageResponseH\x00\x12X\n\x1c\x61ntiklepto_signer_commitment\x18\x05 \x01(\x0b\x32\x30.shiftcrypto.bitbox02.AntiKleptoSignerCommitmentH\x00\x42\n\n\x08response*9\n\x07\x42TCCoin\x12\x07\n\x03\x42TC\x10\x00\x12\x08\n\x04TBTC\x10\x01\x12\x07\n\x03LTC\x10\x02\x12\x08\n\x04TLTC\x10\x03\x12\x08\n\x04RBTC\x10\x04*R\n\rBTCOutputType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05P2PKH\x10\x01\x12\x08\n\x04P2SH\x10\x02\x12\n\n\x06P2WPKH\x10\x03\x12\t\n\x05P2WSH\x10\x04\x12\x08\n\x04P2TR\x10\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'btc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BTCCOIN._serialized_start=5064
  _BTCCOIN._serialized_end=5121
  _BTCOUTPUTTYPE._serialized_start=5123
  _BTCOUTPUTTYPE._serialized_end=5205
  _BTCSCRIPTCONFIG._serialized_start=68
  _BTCSCRIPTCONFIG._serialized_end=650
  _BTCSCRIPTCONFIG_MULTISIG._serialized_start=293
  _BTCSCRIPTCONFIG_MULTISIG._serialized_end=510
  _BTCSCRIPTCONFIG_MULTISIG_SCRIPTTYPE._serialized_start=471
  _BTCSCRIPTCONFIG_MULTISIG_SCRIPTTYPE._serialized_end=510
  _BTCSCRIPTCONFIG_POLICY._serialized_start=512
  _BTCSCRIPTCONFIG_POLICY._serialized_end=587
  _BTCSCRIPTCONFIG_SIMPLETYPE._serialized_start=589
  _BTCSCRIPTCONFIG_SIMPLETYPE._serialized_end=640
  _BTCPUBREQUEST._serialized_start=653
  _BTCPUBREQUEST._serialized_end=1033
  _BTCPUBREQUEST_XPUBTYPE._serialized_start=881
  _BTCPUBREQUEST_XPUBTYPE._serialized_end=1023
  _BTCSCRIPTCONFIGWITHKEYPATH._serialized_start=1035
  _BTCSCRIPTCONFIGWITHKEYPATH._serialized_end=1142
  _BTCSIGNINITREQUEST._serialized_start=1145
  _BTCSIGNINITREQUEST._serialized_end=1511
  _BTCSIGNINITREQUEST_FORMATUNIT._serialized_start=1477
  _BTCSIGNINITREQUEST_FORMATUNIT._serialized_end=1511
  _BTCSIGNNEXTRESPONSE._serialized_start=1514
  _BTCSIGNNEXTRESPONSE._serialized_end=1966
  _BTCSIGNNEXTRESPONSE_TYPE._serialized_start=1836
  _BTCSIGNNEXTRESPONSE_TYPE._serialized_end=1966
  _BTCSIGNINPUTREQUEST._serialized_start=1969
  _BTCSIGNINPUTREQUEST._serialized_end=2203
  _BTCSIGNOUTPUTREQUEST._serialized_start=2206
  _BTCSIGNOUTPUTREQUEST._serialized_end=2549
  _BTCSIGNOUTPUTREQUEST_SILENTPAYMENT._serialized_start=2491
  _BTCSIGNOUTPUTREQUEST_SILENTPAYMENT._serialized_end=2523
  _BTCSCRIPTCONFIGREGISTRATION._serialized_start=2552
  _BTCSCRIPTCONFIGREGISTRATION._serialized_end=2705
  _BTCSUCCESS._serialized_start=2707
  _BTCSUCCESS._serialized_end=2719
  _BTCISSCRIPTCONFIGREGISTEREDREQUEST._serialized_start=2721
  _BTCISSCRIPTCONFIGREGISTEREDREQUEST._serialized_end=2830
  _BTCISSCRIPTCONFIGREGISTEREDRESPONSE._serialized_start=2832
  _BTCISSCRIPTCONFIGREGISTEREDRESPONSE._serialized_end=2892
  _BTCREGISTERSCRIPTCONFIGREQUEST._serialized_start=2895
  _BTCREGISTERSCRIPTCONFIGREQUEST._serialized_end=3147
  _BTCREGISTERSCRIPTCONFIGREQUEST_XPUBTYPE._serialized_start=3098
  _BTCREGISTERSCRIPTCONFIGREQUEST_XPUBTYPE._serialized_end=3147
  _BTCPREVTXINITREQUEST._serialized_start=3149
  _BTCPREVTXINITREQUEST._serialized_end=3247
  _BTCPREVTXINPUTREQUEST._serialized_start=3249
  _BTCPREVTXINPUTREQUEST._serialized_end=3363
  _BTCPREVTXOUTPUTREQUEST._serialized_start=3365
  _BTCPREVTXOUTPUTREQUEST._serialized_end=3427
  _BTCPAYMENTREQUESTREQUEST._serialized_start=3430
  _BTCPAYMENTREQUESTREQUEST._serialized_end=3729
  _BTCPAYMENTREQUESTREQUEST_MEMO._serialized_start=3606
  _BTCPAYMENTREQUESTREQUEST_MEMO._serialized_end=3729
  _BTCPAYMENTREQUESTREQUEST_MEMO_TEXTMEMO._serialized_start=3697
  _BTCPAYMENTREQUESTREQUEST_MEMO_TEXTMEMO._serialized_end=3721
  _BTCSIGNMESSAGEREQUEST._serialized_start=3732
  _BTCSIGNMESSAGEREQUEST._serialized_end=3970
  _BTCSIGNMESSAGERESPONSE._serialized_start=3972
  _BTCSIGNMESSAGERESPONSE._serialized_end=4015
  _BTCREQUEST._serialized_start=4018
  _BTCREQUEST._serialized_end=4659
  _BTCRESPONSE._serialized_start=4662
  _BTCRESPONSE._serialized_end=5062
# @@protoc_insertion_point(module_scope)
