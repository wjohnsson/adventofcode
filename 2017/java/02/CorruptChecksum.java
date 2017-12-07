package adventofcode;

public class CorruptChecksum {
	
	private final static String SPREADSHEET = "1364	461	1438	1456	818	999	105	1065	314	99	1353	148	837	590	404	123\r\n" + 
			"204	99	235	2281	2848	3307	1447	3848	3681	963	3525	525	288	278	3059	821\r\n" + 
			"280	311	100	287	265	383	204	380	90	377	398	99	194	297	399	87\r\n" + 
			"7698	2334	7693	218	7344	3887	3423	7287	7700	2447	7412	6147	231	1066	248	208\r\n" + 
			"3740	837	4144	123	155	2494	1706	4150	183	4198	1221	4061	95	148	3460	550\r\n" + 
			"1376	1462	73	968	95	1721	544	982	829	1868	1683	618	82	1660	83	1778\r\n" + 
			"197	2295	5475	2886	2646	186	5925	237	3034	5897	1477	196	1778	3496	5041	3314\r\n" + 
			"179	2949	3197	2745	1341	3128	1580	184	1026	147	2692	212	2487	2947	3547	1120\r\n" + 
			"460	73	52	373	41	133	671	61	634	62	715	644	182	524	648	320\r\n" + 
			"169	207	5529	4820	248	6210	255	6342	4366	5775	5472	3954	3791	1311	7074	5729\r\n" + 
			"5965	7445	2317	196	1886	3638	266	6068	6179	6333	229	230	1791	6900	3108	5827\r\n" + 
			"212	249	226	129	196	245	187	332	111	126	184	99	276	93	222	56\r\n" + 
			"51	592	426	66	594	406	577	25	265	578	522	57	547	65	564	622\r\n" + 
			"215	2092	1603	1001	940	2054	245	2685	206	1043	2808	208	194	2339	2028	2580\r\n" + 
			"378	171	155	1100	184	937	792	1436	1734	179	1611	1349	647	1778	1723	1709\r\n" + 
			"4463	4757	201	186	3812	2413	2085	4685	5294	5755	2898	200	5536	5226	1028	180";
	
	public static void main(String[] args) {
		System.out.println(checkSum(SPREADSHEET));
//		System.out.println(checkRow("1364	461	1438	1456	818	999	105	1065	314	99	1353	148	837	590	404	123"));
	}
	
	private static int checkSum(String spreadSheet) {
		int sum = 0;
		String[] rows = spreadSheet.split("\r\n");
		
		for (String r : rows) {
			sum += checkRow(r);
		}
		
		return sum;
	}
	
	private static int checkRow(String row) {
		int[] nums = parseString(row.split("\t"));
		int sum = 0;
		
		for (int i = 0; i < nums.length; i++) {
			for (int j = i+1; j < nums.length; j++) {
				if (nums[i] > nums[j]) {
					if (nums[i] % nums[j] == 0) {
						sum += nums[i] / nums[j];
					}
				} else {
					if (nums[j] % nums[i] == 0) {
						sum += nums[j] / nums[i];
					}
				}
			}
		}
		
		return sum;
	}
	
	private static int[] parseString(String[] s) {
		int nums[] = new int[s.length];
		
		for (int i = 0; i < nums.length; i++) {
			nums[i] = Integer.parseInt(s[i]);
		}
		
		return nums;
	}
}
